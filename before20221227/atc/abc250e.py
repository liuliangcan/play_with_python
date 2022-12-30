import sys
from collections import *
from itertools import *
from math import sqrt
from array import *
from functools import lru_cache
import heapq
import bisect
import random
import io, os
from bisect import *

if sys.hexversion == 50924784:
    sys.stdin = open('abcinput.txt')

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())

MOD = 998244353
"""https://atcoder.jp/contests/abc250/tasks/abc250_e

输入 n(≤2e5) 和两个长为 n 的数组 a 和 b，元素范围在 [1,1e9]。
然后输入 q(≤2e5) 表示 q 个询问，每个询问输入两个数 x 和 y，范围在 [1,n]。
对每个询问，设 a 的前 x 个元素去重得到集合 A，b 的前 y 个元素去重得到集合 B，如果 A = B，输出 "Yes"，否则输出 "No"。
输入
5
1 2 3 4 5
1 2 2 4 3
7
1 1
2 2
2 3
3 3
4 4
4 5
5 5
输出
Yes
Yes
Yes
No
No
Yes
No

https://atcoder.jp/contests/abc250/submissions/35814659

为方便处理，首先把数组 a 转换成升序：
例如，先把 31412 置换为 12324，然后求前缀最大值得到 12334（不影响答案的正确性）。

数组 b 也做同样的置换，然后用 https://leetcode.cn/problems/max-chunks-to-make-sorted/ 中提到的技巧，标记 b[i] 应该匹配到 a 中的哪个数。
"""


#    407  	 ms
def solve1(n, a, b, q, qs):
    idx = 0

    def inc():
        nonlocal idx
        idx += 1
        return idx

    hs = defaultdict(inc)

    # 把a、b中的数字都转化成他们的首次出现位置
    for i, v in enumerate(a):
        a[i] = hs[v]
    for i, v in enumerate(b):
        b[i] = hs[v]
    # 求a的前缀最大值
    f = [a[0]] * n
    for i in range(1, n):
        f[i] = max(f[i - 1], a[i])

    # 求b的
    bb = [0] * n
    s = set()
    mx = 0
    for i, v in enumerate(b):
        s.add(v)
        mx = max(mx, v)
        if mx == len(s):
            bb[i] = mx

    ans = ['No'] * q
    for i, (x, y) in enumerate(qs):
        if f[x - 1] == bb[y - 1]:
            ans[i] = 'Yes'

    print('\n'.join(ans))


#    418  	 ms
def solve2(n, a, b, q, qs):
    hs = defaultdict()
    hs.default_factory = hs.__len__

    # 把a、b中的数字都转化成他们的首次出现位置
    for i, v in enumerate(a):
        a[i] = hs[v]
    for i, v in enumerate(b):
        b[i] = hs[v]

    # 求a的前缀最大值
    f = [a[0]] * n
    for i in range(1, n):
        f[i] = max(f[i - 1], a[i])

    # 求b的
    bb = [-1] * n
    s = set()
    mx = 0
    for i, v in enumerate(b):
        s.add(v)
        mx = max(mx, v)
        if mx == len(s) - 1:
            bb[i] = mx

    ans = ['No'] * q
    for i, (x, y) in enumerate(qs):
        if f[x - 1] == bb[y - 1]:
            ans[i] = 'Yes'

    print('\n'.join(ans))


#   408   	 ms
def solve(n, a, b, q, qs):
    hs = defaultdict()
    hs.default_factory = hs.__len__

    # 把a中的数字都转化成他们的首次出现位置;且求前缀最大值
    a = list(accumulate([0] + a, func=lambda x, y: max(x, hs[y])))[1:]
    # 求b能匹配的a最大值
    s, mx = set(), 0
    for i, v in enumerate(b):
        s.add(hs[v])
        mx = max(mx, hs[v])
        b[i] = mx if mx == len(s) - 1 else -1

    ans = ['No'] * q
    for i, (x, y) in enumerate(qs):
        if a[x - 1] == b[y - 1]:
            ans[i] = 'Yes'
    print('\n'.join(ans))


if __name__ == '__main__':
    n, = RI()
    a = RILST()
    b = RILST()
    q, = RI()
    qs = []
    for _ in range(q):
        qs.append(RILST())
    solve(n, a, b, q, qs)
