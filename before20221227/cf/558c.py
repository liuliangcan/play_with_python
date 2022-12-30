import sys
from collections import *
from itertools import *
from math import *
from array import *
from functools import lru_cache
import heapq
import bisect
import random
import io, os
from bisect import *

if sys.hexversion == 50924784:
    sys.stdin = open('cfinput.txt')

# input = sys.stdin.readline
# input_int = sys.stdin.buffer.readline
# RI = lambda: map(int, input_int().split())
# RS = lambda: input().strip().split()
# RILST = lambda: list(RI())

# RI = lambda: map(int, sys.stdin.buffer.readline().split())
# RS = lambda: sys.stdin.readline().strip().split()
# RILST = lambda: list(RI())

# input = sys.stdin.buffer.readline
# RI = lambda: map(int, input().split())
# RS = lambda: map(bytes.decode, input().strip().split())
# RILST = lambda: list(RI())

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())

MOD = 10 ** 9 + 7
"""输入https://codeforces.com/problemset/problem/558/C

输入 n(≤1e5) 和一个长为 n 的数组 a (1≤a[i]≤1e5)。
每次操作你可以将某个 a[i] 乘二或除二（下取整）。
输出至少需要多少次操作，可以让 a 的所有数都相同。
3
4 8 2
输出 2
解释 都变成 4。

输入
3
3 5 6
输出 5
解释 都变成 1。
"""


#  tle ms
def solve1(n, a):
    # cnt = [0] * (max(a) + 1)
    # for v in a:
    #     cnt[v] += 1
    mx = max(a)
    cnt = Counter(a)
    if len(cnt) <= 1:
        return 0
    cnt = sorted([(k, v) for k, v in cnt.items()], key=lambda x: (x[1], x[0]), reverse=True)

    # @lru_cache
    def calc(a, b):
        if a == b:
            return 0
        elif a < b:
            s = b // a
            if s * a == b and s & (s - 1) == 0:
                return int(log2(s))
        elif a > b:
            s = a // b
            if s * b == a and s & (s - 1) == 0:
                return int(log2(s))

        ans = 0
        while b and b & 1 == 0:
            ans += 1
            b >>= 1
        while a > b:
            ans += 1
            a >>= 1
            if a == b:
                return ans

        return inf

    top = sum(calc(k, 1) * v for k, v in cnt)

    k, c = cnt[0]
    vis = {k: 0}
    q = deque([k])
    step = 0
    while q:
        step += c
        if step + n - c > top:
            break
        for _ in range(len(q)):
            u = q.popleft()
            for v in u << 1, u >> 1:
                if v and v <= mx and v not in vis:
                    vis[v] = step
                    q.append(v)

    print(top, vis, )

    for i in range(1, len(cnt)):
        k, v = cnt[i]
        c += v
        pre = vis
        vis = {}

        for a, b in pre.items():
            step = calc(k, a)
            if step == 0:
                vis[a] = b
            else:
                step = step * v + b
                if step <= top:
                    vis[a] = step

            # print(i, cnt[i], vis,step,a,b,s)
        # print(i, cnt[i], vis)
    print(min(vis.values()))


#  	 ms
def solve2(n, a):
    # cnt = [0] * (max(a) + 1)
    # for v in a:
    #     cnt[v] += 1
    cnt = Counter(a)
    if len(cnt) <= 1:
        return 0
    cnt = sorted([(k, v) for k, v in cnt.items()], key=lambda x: (x[1], x[0]), reverse=True)

    @lru_cache
    def calc(a, b):
        if a == b:
            return 0
        elif a < b:
            s = b // a
            if s * a == b and s & (s - 1) == 0:
                return int(log2(s))
        elif a > b:
            if b == 1:
                ans = 0
                while a > b:
                    ans += 1
                    a >>= 1
                return ans

            s = a // b
            if s * b == a and s & (s - 1) == 0:
                return int(log2(s))

        ans = 0
        while b and b & 1 == 0:
            ans += 1
            b >>= 1
        while a > b:
            ans += 1
            a >>= 1
            if a == b:
                return ans

        return inf

    top = sum(calc(k, 1) * v for k, v in cnt)  # 最多全变1

    mn = inf
    mnk = 0
    for i, (k, _) in enumerate(cnt):
        t = 0
        while k and k & 1 == 0:
            t += 1
            k >>= 1
        if 1 < k < mn:
            mn = k
            mnk = cnt[i][0]
    if mn < inf:  # 有奇数
        ans = 0
        for k, v in cnt:
            p = calc(k, mnk)
            if p == inf:
                return print(top)
            ans += p * v
        return print(ans)
    # 没奇数
    print(min(sum(calc(k, 1 << x) * v for k, v in cnt) for x in range(21)))


def solve(n, a):
    mx = max(a)
    cnt = [0] * (mx + 1)  # 访问次数
    s = [0] * (mx + 1)  # 总步数
    q = deque()
    vis = [-1] * (mx + 1)
    for i, v in enumerate(a):
        cnt[v] += 1
        q.append(v)
        vis[v] = i
        step = 0
        while q:
            step += 1
            for _ in range(len(q)):
                u = q.popleft()
                for v in u >> 1, u << 1:
                    if v and v <= mx and vis[v] != i:
                        vis[v] = i
                        cnt[v] += 1
                        s[v] += step
                        q.append(v)

    print(min(b for a, b in zip(cnt, s) if a == n))


if __name__ == '__main__':
    n, = RI()
    a = RILST()

    solve(n, a)
