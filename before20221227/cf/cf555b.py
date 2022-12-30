import sys
from bisect import *
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

input = sys.stdin.readline
input_int = sys.stdin.buffer.readline
RI = lambda: map(int, input_int().split())
RS = lambda: input().strip().split()
RILST = lambda: list(RI())

MOD = 10 ** 9 + 7
"""https://codeforces.com/problemset/problem/555/B

输入 n(2≤n≤2e5) 和 m(1≤m≤2e5)，
然后输入 n 行，每行有两个数，表示一个闭区间（1≤L≤R≤1e18），
然后输入一个长为 m 的数组 a (1≤a[i]≤1e18)。
输入保证区间之间没有交集，且上一个区间的右端点小于下一个区间的左端点。

你有 m 座桥，每座桥的长为 a[i]，你需要选择 n-1 座桥连接所有相邻的区间。
要求桥的两个端点需要分别落在这两个闭区间内（这两个端点的差等于桥长）。

如果无法做到，输出 No；否则输出 Yes，然后按顺序输出这 n-1 座桥的编号（编号从 1 开始），输出的第一座桥连接第一个区间和第二个区间，输出的第二座桥连接第二个区间和第三个区间，依此类推。

思考：如果不要求连接的两个区间相邻，你能否连通所有区间？
输入
4 4
1 4
7 8
9 10
12 14
4 5 3 8
输出
Yes
2 3 1 

输入
2 2
11 14
17 18
2 9
输出
No

输入
2 1
1 1
1000000000000000000 1000000000000000000
999999999999999999
输出
Yes
1 
"""


# 匈牙利TLE	m*n*n
def solve1(n, m, lr, a):
    n -= 1
    if m < n:
        return print('No')
    a.sort()  # test
    a = [0] + a
    pos = []
    for i in range(n):
        l1, r1 = lr[i]
        l2, r2 = lr[i + 1]
        pos.append([l2 - r1, r2 - l1])
    ans = [0] * n
    vis = [0] * n

    def find(i):
        for j in range(n):
            if (pos[j][0] <= a[i] <= pos[j][1]) and not vis[j]:
                vis[j] = 1
                if ans[j] == 0 or find(ans[j]):
                    ans[j] = i
                    return True
        return False

    cnt = 0
    for i in range(1, m + 1):
        if find(i):
            cnt += 1
    if cnt == n:
        print('Yes')
        return print(' '.join(map(str, ans)))
    print('No')


# 2027 ms 贪心 pos按l排序，遍历a，双指针遍历pos，堆维护已访问的pos
def solve(n, m, lr, a):
    n -= 1
    if m < n:
        return print('No')
    a = sorted([(v, i) for i, v in enumerate(a)])

    pos = []
    for i in range(n):
        l1, r1 = lr[i]
        l2, r2 = lr[i + 1]
        l, r = l2 - r1, r2 - l1
        if l > a[-1][0] or r < a[0][0]:
            return print('No')
        pos.append([l, r])

    pos = sorted([(l, r, i) for i, (l, r) in enumerate(pos)])

    ans = [0] * n
    j = 0
    h = []
    for v, i in a:
        while j < n and pos[j][0] <= v:
            l, r, idx = pos[j]
            heapq.heappush(h, (r, idx))
            j += 1
        if h and h[0][0] < v:  # r在v左边的坑，永远也填不上了
            return print('No')
            # heapq.heappop(h)
        if not h:  # 没有l在左边的数据了，放不了
            continue

        _, idx = heapq.heappop(h)
        ans[idx] = i + 1
    if j < n:
        return print('No')
    print('Yes')
    return print(' '.join(map(str, ans)))


# SortedList 1902ms pos按r排序，遍历pos使用最小的桥移除使用过的桥
def solve2(n, m, lr, a):
    n -= 1
    if m < n:
        return print('No')
    from sortedcontainers import SortedList
    a = SortedList([(v, i) for i, v in enumerate(a)])

    pos = []
    for i in range(n):
        l1, r1 = lr[i]
        l2, r2 = lr[i + 1]
        l, r = l2 - r1, r2 - l1
        if l > a[-1][0] or r < a[0][0]:
            return print('No')
        pos.append([l, r])

    pos = sorted([(l, r, i) for i, (l, r) in enumerate(pos)], key=lambda x: x[1])

    ans = [0] * n
    for l, r, i in pos:
        p = a.bisect_left((l, -1))
        if a[p][0] <= r:
            ans[i] = a[p][1]+1
            a.pop(p)
        else:
            return print('No')

    print('Yes')
    return print(' '.join(map(str, ans)))

if __name__ == '__main__':
    # import sys
    #
    # print(sys.version)
    # print(sys.version_info)
    # from sortedcontainers import SortedList
    n, m = RI()
    lr = []
    for _ in range(n):
        l, r = RI()
        lr.append([l, r])
    a = RILST()
    solve(n, m, lr, a)
