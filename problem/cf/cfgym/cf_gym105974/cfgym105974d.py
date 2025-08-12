# Problem: D. Range Xor Subsequence Query
# Contest: Codeforces - Introductory Problems: XOR Basis
# URL: https://codeforces.com/gym/105974/problem/D
# Memory Limit: 256 MB
# Time Limit: 2000 ms

import sys

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())


class PrefixXorBasis:
    def __init__(self, a, n):
        # self.n = n
        self.bs = bs = []
        self.ps = ps = []
        b = [0] * n
        p = [-1] * n
        for i, x in enumerate(a):
            while x:
                j = x.bit_length() - 1
                if b[j] == 0:
                    b[j] = x
                    p[j] = i
                    break
                if p[j] < i:
                    p[j], i = i, p[j]
                    x, b[j] = b[j], x
                x ^= b[j]
            bs.append(b[:])
            ps.append(p[:])

    def get_basis_less(self, l, r):  # 获取[l,r]的线性基,0-based,去掉0的
        return [x for x, y in zip(self.bs[r], self.ps[r]) if y >= l]

    def get_basis(self, l, r):  # 获取[l,r]的线性基,0-based
        return [x if y >= l else 0 for x, y in zip(self.bs[r], self.ps[r])]

    def can_present(self, l, r, x):  # [l,r]里能否表出x,0-based
        p = self.ps[r]
        if x == 0:
            return len([1 for i in p if i >= l]) < r - l + 1
        else:
            b = self.bs[r]
            while x:
                i = x.bit_length() - 1
                if b[i] == 0 or p[i] < l:
                    return False
                x ^= b[i]
            return True



#        ms
def solve():
    n, = RI()
    a = RILST()
    pb = PrefixXorBasis(a, 60)

    q, = RI()
    for _ in range(q):
        l, r, x = RI()
        print('Yes' if pb.can_present(l - 1, r - 1, x) else 'No')


#        ms
def solve4():
    n, = RI()
    a = RILST()
    pb = PrefixXorBasis(a, 60)

    q, = RI()
    for _ in range(q):
        l, r, x = RI()
        b = pb.get_basis(l - 1, r - 1)
        if x == 0:
            print('Yes' if len(b) == r - l + 1 else 'No')
        else:
            while x:
                i = x.bit_length() - 1
                if b[i] == 0:
                    print('No')
                    break
                x ^= b[i]
            else:
                print('Yes')


#    1749    ms
def solve3():
    n, = RI()
    a = RILST()
    pb = PrefixXorBasis(a, 60)

    q, = RI()
    for _ in range(q):
        l, r, x = RI()
        b = pb.get_basis(l - 1, r - 1)
        if x == 0:
            print('Yes' if len(b) == r - l + 1 else 'No')
        else:
            for v in b[::-1]:
                x = min(x, x ^ v)
            print('Yes' if x == 0 else 'No')


#    1671   ms
def solve2():
    n, = RI()
    a = RILST()
    b = [(1 << (59 - i), -1) for i in range(60)]
    bs = [b]
    for i, x in enumerate(a):
        for j, (v, p) in enumerate(b):
            if x > x ^ v:
                if p < i:
                    b[j] = x, i
                    i = p
                x ^= v

        bs.append(b[:])

    q, = RI()
    for _ in range(q):
        l, r, x = RI()
        b = bs[r]
        if x == 0:
            if len(b) == r - l + 1:
                print('No')
            else:
                print('Yes')
        else:
            for v, i in b:
                if i + 1 >= l and x ^ v < x:
                    x ^= v
            print('Yes' if x == 0 else 'No')


#    1327    ms
def solve1():
    n, = RI()
    a = RILST()
    b = [0] * 60
    p = [-1] * 60
    bs = []
    ps = []
    for i, x in enumerate(a):
        while x:
            j = x.bit_length() - 1
            if b[j] == 0:
                b[j] = x
                p[j] = i
                break
            if p[j] < i:
                p[j], i = i, p[j]
                x, b[j] = b[j], x
            x ^= b[j]
        bs.append(b[:])
        ps.append(p[:])

    q, = RI()
    for _ in range(q):
        l, r, x = RI()
        b = bs[r - 1]
        p = ps[r - 1]
        if x == 0:
            d = len([1 for i in p if i + 1 >= l])
            if d == r - l + 1:
                print('No')
            else:
                print('Yes')
        else:
            while x:
                i = x.bit_length() - 1
                if b[i] and p[i] + 1 >= l:
                    x ^= b[i]
                else:
                    print('No')
                    break
            else:
                print('Yes')


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
