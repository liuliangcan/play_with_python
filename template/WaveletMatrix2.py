''' 这个不能求和，但是快40%
W = WMCompressed(A)             离散化小波矩阵
W.kth(k, l, r)                  功能：在区间 [l,r) 内返回第 k 小的真实值 (k从0开始)
W.select(y, k, l=0, r=-1)       功能：返回 y 在 [l,r) 内第 k 次出现的位置 (k从0开始)
W.count(y, l, r)                功能：统计 [l,r) 内 y 的出现次数
W.count_below(u, l, r)          功能：统计区间 [l,r) 内 < u 的元素个数。
W.count_between(d, u, l, r)     功能：统计区间 [l,r) 内 d <= x < u 的数量。
W.prev_val(u, l, r)             功能：返回区间 [l,r) 内 < u 的最大值。
W.next_val(d, l, r)             功能：返回区间 [l,r) 内 >= d 的最小值。
'''
from array import array

def u32f(N: int, elm: int = 0):
    return array('I', (elm,)) * N  # unsigned int

def bisect_left(A, x, l, r):
    while l < r:
        if A[m := (l + r) >> 1] < x:
            l = m + 1
        else:
            r = m
    return l

def bisect_right(A, x, l, r):
    while l < r:
        if x < A[m := (l + r) >> 1]:
            r = m
        else:
            l = m + 1
    return l

def coord_compress(A: list[int], distinct=False):
    s, m = pack_sm((N := len(A)) - 1);
    R, V = [0] * N, [a << s | i for i, a in enumerate(A)];
    V.sort()
    if distinct:
        for r, ai in enumerate(V): a, i = pack_dec(ai, s, m); R[i], V[r] = r, a
    else:
        r = p = -1
        for ai in V:
            a, i = pack_dec(ai, s, m)
            if a != p: r = r + 1; V[r] = p = a
            R[i] = r
        del V[r + 1:]
    return R, V

def pack_sm(N: int):
    s = N.bit_length()
    return s, (1 << s) - 1

def pack_enc(a: int, b: int, s: int):
    return a << s | b

def pack_dec(ab: int, s: int, m: int):
    return ab >> s, ab & m

def pack_indices(A, s):
    return [a << s | i for i, a in enumerate(A)]

class BitArray:
    def __init__(B, N: int):
        B.N, B.Z = N, (N + 31) >> 5
        B.bits, B.cnt = u32f(B.Z + 1), u32f(B.Z + 1)

    def build(B):
        B.bits.pop()
        for i, b in enumerate(B.bits): B.cnt[i + 1] = B.cnt[i] + popcnt32(b)
        B.bits.append(0)

    def __len__(B):
        return B.N

    def __getitem__(B, i: int):
        return B.bits[i >> 5] >> (31 - (i & 31)) & 1

    def set0(B, i: int):
        B.bits[i >> 5] &= ~(1 << 31 - (i & 31))

    def set1(B, i: int):
        B.bits[i >> 5] |= 1 << 31 - (i & 31)

    def count0(B, r: int):
        return r - B.count1(r)

    def count1(B, r: int):
        return B.cnt[r >> 5] + popcnt32(B.bits[r >> 5] >> 32 - (r & 31))

    def select0(B, k: int):
        if not 0 <= k < B.N - B.cnt[-1]: return -1
        l, r, k = 0, B.N, k + 1
        while 1 < r - l:
            if B.count0(m := (l + r) >> 1) < k:
                l = m
            else:
                r = m
        return l

    def select1(B, k: int):
        if not 0 <= k < B.cnt[-1]: return -1
        l, r, k = 0, B.N, k + 1
        while 1 < r - l:
            if B.count1(m := (l + r) >> 1) < k:
                l = m
            else:
                r = m
        return l

def popcnt32(x):
    x = ((x >> 1) & 0x55555555) + (x & 0x55555555)
    x = ((x >> 2) & 0x33333333) + (x & 0x33333333)
    x = ((x >> 4) & 0x0f0f0f0f) + (x & 0x0f0f0f0f)
    x = ((x >> 8) & 0x00ff00ff) + (x & 0x00ff00ff)
    x = ((x >> 16) & 0x0000ffff) + (x & 0x0000ffff)
    return x

class WMStatic:
    class Level(BitArray):
        def __init__(L, N: int, H: int):
            super().__init__(N)
            L.H = H

        def build(L):
            super().build()
            L.T0, L.T1 = L.N - L.cnt[-1], L.cnt[-1]

        def pos(L, bit: int, i: int): return L.T0 + L.count1(i) if bit else L.count0(i)

        def pos2(L, bit: int, i: int, j: int): return (L.T0 + L.count1(i), L.T0 + L.count1(j)) if bit else (L.count0(i),
                                                                                                            L.count0(j))

    def __init__(wm, A, Amax: int = None):
        if Amax is None: Amax = max(A, default=0)
        wm._build(A, [0] * len(A), Amax)

    def _build(wm, A, nA, Amax):
        wm.N = N = len(A);
        wm.H = Amax.bit_length()
        wm.up = [WMStatic.Level(N, H) for H in range(wm.H)];
        wm.down = wm.up[::-1]
        for L in wm.down:
            x, y, i = -1, N - 1, N
            while i: y -= A[i := i - 1] >> L.H & 1
            for i, a in enumerate(A):
                if a >> L.H & 1:
                    nA[y := y + 1] = a;L.set1(i)
                else:
                    nA[x := x + 1] = a
            A, nA = nA, A;
            L.build()

    def kth(wm, k: int, l: int, r: int):
        if k < 0: k += r - l
        s = 0
        for L in wm.down:
            l, r = l - (l1 := L.count1(l)), r - (r1 := L.count1(r))
            if k >= r - l: s |= 1 << L.H;k -= r - l;l, r = L.T0 + l1, L.T0 + r1
        return s

    def select(wm, y: int, k: int, l: int = 0, r: int = -1):
        if not (0 <= y < 1 << wm.H): return -1
        if r == -1: r = wm.N - 1
        if k < 0: k += r - l
        for L in wm.down: l, r = L.pos2(L[y], l, r)
        if not l <= (i := l + k) < r: return -1
        for L in wm.up:
            if y >> L.H & 1:
                i = L.select1(i - L.T0)
            else:
                i = L.select0(i)
        return i

    def count(wm, y: int, l: int, r: int):
        if l >= r: return 0
        return wm._cnt(y + 1, l, r) - wm._cnt(y, l, r)

    def count_below(wm, u: int, l: int, r: int):
        return wm._cnt(u, l, r)

    def count_between(wm, d: int, u: int, l: int, r: int):
        if l >= r or d >= u: return 0
        return wm._cnt(u, l, r) - wm._cnt(d, l, r)

    def _cnt(wm, u: int, l: int, r: int):
        if u <= 0: return 0
        if u.bit_length() > wm.H: return r - l
        cnt = 0
        for L in wm.down:
            l, r = l - (l1 := L.count1(l)), r - (r1 := L.count1(r))
            if u >> L.H & 1: cnt += r - l;l, r = L.T0 + l1, L.T0 + r1
        return cnt

    def prev_val(wm, u: int, l: int, r: int):
        return wm.kth(cnt - 1, l, r) if (cnt := wm._cnt(u, l, r)) else -1

    def next_val(wm, d: int, l: int, r: int):
        return wm.kth(cnt, l, r) if (cnt := wm._cnt(d, l, r)) < r - l else -1

class WMCompressed(WMStatic):
    def __init__(wm, A): A, wm.Y = coord_compress(A);super().__init__(A, len(wm.Y) - 1)

    def _didx(wm, y: int): return bisect_left(wm.Y, y, 0, len(wm.Y))

    def _uidx(wm, y: int): return bisect_right(wm.Y, y, 0, len(wm.Y))

    def _yidx(wm, y: int): return i if (i := wm._didx(y)) < len(wm.Y) and wm.Y[i] == y else -1

    def __contains__(wm, y: int): return (i := wm._didx(y)) < len(wm.Y) and wm.Y[i] == y

    def kth(wm, k, l, r): return wm.Y[super().kth(k, l, r)]

    def select(wm, y, k, l=0, r=-1): return super().select(y, k, l, r) if ~(y := wm._yidx(y)) else -1

    def count(wm, y, l, r): return super().count(y, l, r) if ~(y := wm._yidx(y)) else 0

    def count_below(wm, u, l, r): return super().count_below(wm._didx(u), l, r)

    def count_between(wm, d, u, l, r): return super().count_between(wm._didx(d), wm._didx(u), l, r)

    def prev_val(wm, u, l, r): return super().prev_val(wm._didx(u), l, r)

    def next_val(wm, d, l, r): return super().next_val(wm._didx(d), l, r)

'''
W = WMCompressed(A)             离散化小波矩阵
W.kth(k, l, r)                  功能：在区间 [l,r) 内返回第 k 小的真实值 (k从0开始)
W.select(y, k, l=0, r=-1)       功能：返回 y 在 [l,r) 内第 k 次出现的位置 (k从0开始)
W.count(y, l, r)                功能：统计 [l,r) 内 y 的出现次数
W.count_below(u, l, r)          功能：统计区间 [l,r) 内 < u 的元素个数。
W.count_between(d, u, l, r)     功能：统计区间 [l,r) 内 d <= x < u 的数量。
W.prev_val(u, l, r)             功能：返回区间 [l,r) 内 < u 的最大值。
W.next_val(d, l, r)             功能：返回区间 [l,r) 内 >= d 的最小值。
'''

from sys import stdin
input = lambda: stdin.readline().rstrip()

def solve():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    W = WMCompressed(A)
    for _ in range(Q):
        l, r, k = map(int, input().split())
        print(W.kth(k - 1, l - 1, r))

solve()