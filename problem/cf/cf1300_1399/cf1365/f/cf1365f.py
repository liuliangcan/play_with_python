# Problem: F. Swaps Again
# Contest: Codeforces - Codeforces Round 648 (Div. 2)
# URL: https://codeforces.com/problemset/problem/1365/F
# Memory Limit: 256 MB
# Time Limit: 2000 ms

import sys
import bisect
import random
import io, os
from bisect import *
from collections import *
from contextlib import redirect_stdout
from itertools import *
from array import *
from functools import lru_cache
from types import GeneratorType
from heapq import *
from math import sqrt, gcd, inf

if sys.version >= '3.8':  # ACW没有comb
    from math import comb

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')

MOD = 10 ** 9 + 7
PROBLEM = """https://codeforces.com/problemset/problem/1365/F

输入 t(≤500) 表示 t 组数据。
每组数据输入 n(≤500) 和两个长为 n 的数组 a b，元素范围在 [1,1e9]。

你可以执行如下操作任意次：
首先选择一个在 [1,n/2] 范围内的整数 k，然后交换 a 的长为 k 的前缀与长为 k 的后缀。
例如 [1,2,3,4,5,6] k=2 交换后为 [5,6,3,4,1,2]
a 能否变成 b？输出 Yes 或 No。

进阶：如果可以做到，用 3n/2 次操作完成。
输入
5
2
1 2
2 1
3
1 2 3
1 2 3
3
1 2 4
1 3 4
4
1 2 3 2
3 1 2 2
3
1 2 3
1 3 2
输出 
Yes
Yes
No
Yes
No
"""
"""https://codeforces.com/problemset/submission/1365/199894156

提示 1：操作不会改变什么性质？

提示 2：如果两个数 x y 在交换前关于 n/2 对称，那么交换后也是对称的（即便位置变了）
统计 a 中对称位置组成的数对及其个数，b 中对称位置组成的数对及其个数。
如果所有个数都相同，则方案存在。（注意 n 为奇数时 a[n/2] 需要等于 b[n/2]）

具体可以从内向外构造
例如 abczyx 变成 xcybza，可以先从最内部的 yb 开始。
abczyx -> yxczab -> bxczay -> zaybxc
k 分别是 2,1,3（把 y 和 b 移动到最外侧，然后交换到内侧）

然后解决 cz，k=2 即可：
zaybxc -> xcybza"""
"""补充：
观察12345,k=2，交换一次变成45312，本来1对应5，交换完了1还是对应5。
因此这个关系是不变的，a和b中的关系对数必须相同。
相同时是否一定有答案呢，一定有，方法就是灵神题解中的构造部分。
每次把b最内侧的对，在a中找到，交换到最外侧，然后翻转到内侧即可；之后的操作就可以不再碰已处理过的部分。
因此一定有答案。
"""

#    280   ms
def solve():
    n, = RI()
    a = RILST()
    b = RILST()
    if n & 1 and a[n // 2] != b[n // 2]:
        return print('No')
    cnt = Counter()
    l, r = 0, n - 1
    while l < r:
        x, y = a[l], a[r]
        if x < y:
            x, y = y, x
        cnt[(x, y)] += 1
        x, y = b[l], b[r]
        if x < y:
            x, y = y, x
        cnt[(x, y)] -= 1
        l += 1
        r -= 1

    if any(x != 0 for x in cnt.values()):
        return print('No')
    print('Yes')


if __name__ == '__main__':
    t, = RI()
    for _ in range(t):
        solve()
