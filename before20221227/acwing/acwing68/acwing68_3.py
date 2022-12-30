import collections
import io
import os
import sys
from bisect import bisect_right
from collections import *
from itertools import accumulate
from math import inf

if sys.hexversion == 50923504:
    sys.stdin = open('input.txt')
    RI = lambda: map(int, input().split())
else:
    input = sys.stdin.readline
    input_int = sys.stdin.buffer.readline
    RI = lambda: map(int, input_int().split())

RS = lambda: input().strip().split()
RILST = lambda: list(RI())

MOD = 10 ** 9 + 7


def solve(n, m, q, w, S, Q):
    # print(w)
    query = [[] for _ in range(1<<n)]
    ans = [0] * q
    for i, (t, k) in enumerate(Q):
        query[t].append((k, i))
    ss = [0] * (1 << n)
    for s in S:
        ss[s] += 1
    for t, kis in enumerate(query):
        if len(kis) == 0:
            continue
        # mx = max(k for k, i in kis)
        vs = [0] * 101
        for s, cnt in enumerate(ss):
            a = t ^ s
            # a = a ^ ((1 << n) - 1)
            # print(s,a,cnt)
            v = 0
            for i in range(n):
                if (a>>i&1) == 0:
                    v += w[i]
            if v <= 100:
                vs[v] += cnt
        # vs = sorted([(k, v) for k, v in enumerate(vs)])
        pre = list(accumulate([v for k, v in enumerate(vs)]))
        # print(vs)
        # print(pre)
        pos = 0
        kis.sort()
        # print(kis)
        for k, i in kis:
            while pos < 101 and pos <= k:
                pos += 1
            # pos = bisect_right(vs, (k,inf))
            ans[i] = pre[pos - 1]
    for i in ans:
        print(i)


if __name__ == '__main__':
    n, m, q = RI()
    w = RILST()
    S = []
    for _ in range(m):
        s, = RS()
        S.append(int(s, 2))
    Q = []


    a = gcd(3,2)
    for _ in range(q):
        t, k = RS()
        Q.append([int(t, 2), int(k)])
    solve(n, m, q, w[::-1], S, Q)
