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

if sys.hexversion == 50924784:
    sys.stdin = open('cfinput.txt')
    RI = lambda: map(int, input().split())
else:
    input = sys.stdin.readline
    input_int = sys.stdin.buffer.readline
    RI = lambda: map(int, input_int().split())

RS = lambda: input().strip().split()
RILST = lambda: list(RI())

MOD = 10 ** 9 + 7
"""https://codeforces.com/problemset/problem/1619/E

输入 t (≤1e4) 表示 t 组数据，每组数据输入输入 n(≤2e5) 和一个长为 n 的数组 a (0≤a[i]≤n)。所有数据的 n 之和不超过 2e5。
每次操作，你可以把数组中的一个数加一。
定义 mex(a) 表示不在 a 中的最小非负整数。
定义 f(i) 表示使 mex(a) = i 的最小操作次数。如果无法做到，则 f(i) = -1。
输出 n+1 个数：f(0), f(1), ..., f(n)。

输入
5
3
0 1 3
7
0 1 2 3 4 3 2
4
3 0 0 0
7
4 6 2 3 5 0 5
5
4 0 1 0 4
输出
1 1 0 -1 
1 1 2 2 1 0 2 6 
3 0 1 4 3 
1 0 -1 -1 -1 -1 -1 -1 
2 1 0 2 -1 -1 
"""


# heap	514  ms
def solve1(n, a):
    ans = [-1] * (n + 1)
    cnt = [0] * (n + 1)
    for v in a:
        cnt[v] += 1
    pre = [0] + list(accumulate(cnt))
    s = 0
    h = []
    for i in range(n + 1):
        if pre[i] < i:
            break
        c = cnt[i]
        ans[i] = s + c
        if c > 1:
            heapq.heappush(h, [-i, c - 1])
        elif c == 0:
            if not h:
                break
            s += i + h[0][0]
            if h[0][1] == 1:
                heapq.heappop(h)
            else:
                h[0][1] -= 1

    print(' '.join(map(str, ans)))


# stack	202  ms
def solve(n, a):
    ans = [-1] * (n + 1)
    cnt = [0] * (n + 1)
    for v in a:
        cnt[v] += 1
    # pre = [0] + list(accumulate(cnt))
    s = 0
    st = []
    for i in range(n + 1):
        # if pre[i] < i:
        #     break
        c = cnt[i]
        ans[i] = s + c
        if c > 1:
            st.append([i, c - 1])
        elif c == 0:
            if not st:
                break
            s += i - st[-1][0]
            if st[-1][1] == 1:
                st.pop()
            else:
                st[-1][1] -= 1

    print(' '.join(map(str, ans)))


if __name__ == '__main__':
    t, = RI()
    for _ in range(t):
        n, = RI()
        a = RILST()

        solve(n, a)
