import io
import os
from collections import defaultdict




def solve():
    n, k = map(int, input().split())

    p = [0] + list([int(s)-1 for s in input().split()])

    lo = 0
    hi = n

    while lo + 1 < hi:
        mid = (lo + hi) // 2

        cost = 0
        max_depth = [0] * n
        for v in range(n-1, 0, -1):
            if p[v] == 0:
                continue
            if max_depth[v] >= mid - 1:
                cost += 1
            else:
                max_depth[p[v]] = max(max_depth[p[v]], max_depth[v] + 1)
        if cost <= k:
            hi = mid
        else:
            lo = mid
    print(hi)


t = int(input())

for _ in range(t):
    solve()

# 这个case会wa，因为没处理顺序
"""
2
6 0
3 4 5 6 1
6 1
3 4 5 6 1

# 答案是
5
3
"""
