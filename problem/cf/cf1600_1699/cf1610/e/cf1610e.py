# Problem: E. AmShZ and G.O.A.T.
# Contest: Codeforces - Codeforces Global Round 17
# URL: https://codeforces.com/problemset/problem/1610/E
# Memory Limit: 256 MB
# Time Limit: 1000 ms

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
PROBLEM = """https://codeforces.com/problemset/problem/1610/E

输入 t(≤1e4) 表示 t 组数据。所有数据的 n 之和 ≤2e5。
每组数据输入 n(2≤n≤2e5) 和长为 n 的有序数组 a(1≤a[i]≤1e9)，有重复元素。

你需要从 a 中删除一些元素，使得对于 a 的任意非空子序列 b，都必须满足：
设 avg 为 b 的平均值（可以是小数），b 中比 avg 小的数的个数必须 >= b 中比 avg 大的数的个数。

例如 [1,4,4,5,6] 的平均值为 4，有 1 个数比 4 小，有 2 个数比 4 大，这是不满足要求的。
而 [4,4,5,6] 是满足要求的。

最少需要删除多少个数？

注：子序列不要求连续。
输入
4
3
1 2 3
5
1 4 4 5 6
6
7 8 197860736 212611869 360417095 837913434
8
6 10 56026534 405137099 550504063 784959015 802926648 967281024
输出
0
1
2
3
"""
"""https://codeforces.com/problemset/submission/1610/200982867

提示 1：长为 3 的子序列需要满足什么性质？

设这三个数分别为 x，y，z，那么 y <= avg = (x+y+z)/3，变形得 z >= 2y-x = 2(y-x)+x

提示 2：在长为 3 的子序列的基础上，增加一个数，这个数需要满足什么性质？

设增加的数为 u，那么 x，z，u 必须是满足要求的，即 u >= 2z-x >= 2(2y-x)-x = 4y-3x = 4(y-x)+x

依此类推，增加的数必须 >= 2^k*(y-x)+x，这是指数增长的，所以子序列 b 的长度不会超过 log(max(a))。

这样就可以暴力了，为了让去掉的数尽量少，那么保留的数要尽量多。
1. y-x 尽量小（但不能为 0），那么枚举所有 a[i] != a[i+1] 作为 x 和 y。
2. 从 x,y 开始构建子序列 b，二分找下一个数。

注意重复元素，所有重复的 x 都可以保留。"""
"""构造+贪心+枚举+通过倍增考虑复杂度
题目问最少删除几个数，等价于问最多保留几个数。考虑保留的序列的性质。
- 结论1：若保留的数据里有重复，只允许mn重复。
    - 一旦其它数据重复，假设是k，那么取子序列[mn,k,k],则有mn<avg<k，显然不合法。
    - 若mn重复则不影响。因为只会使avg向左偏移最多1个数，但左边也增加了一个数字mn。
- 结论2：假设保留的数据按顺序是[a...b,c] (不重复)，那么最有可能不合法的情况是[a,b,c]，因为bc离得较近，a太小，更有可能使avg<b。
- 结论3：为了令结论2中的情况合法，我们需要让avg右移超过b。方法是让c足够大，具体多大：(a+b+c)/3>=b,得c>=2b-a。
    - 设想在[a..b]的基础上添加c，由于abc不重复，添加的c距离b的长度一定超过b对a的长度，即每次添加完数据，序列的首尾距离至少是倍增的。
    - 那么构造整个序列需要的次数不会超过logU。
    - 同时添加的c要越小越好（贪心，这样才更有可能在c后边继续添加），这里可以二分。
- 做法：遍历每个数作为保留序列的最小值mn，向后贪心的添加可能的c，直到c超过max(a)，则没有数据可以添加。
- 复杂度：构造每组数据时，最多添加logn个c，每次找c要二分，因此总体复杂度O(nlogUlogn)
"""


# 763 ms
def solve():
    n, = RI()
    a = RILST()
    cnt = Counter(a)
    # if len(cnt) == 1:
    #     return print(0)
    # elif len(cnt) == 2:
    #     a = sorted(cnt.keys())
    #     return print(n - max(cnt[a[1]], cnt[a[0]] + 1))
    ans = 2  # 最多能保留几个数
    for mn, c in cnt.items():
        mx = mn
        keep = c
        p = bisect_left(a, max(mx * 2 - mn, mn + 1))
        while p < n:
            mx = a[p]
            keep += 1
            p = bisect_left(a, max(mx * 2 - mn, mn + 1))
        ans = max(ans, keep)
    print(n - ans)


if __name__ == '__main__':
    t, = RI()
    for _ in range(t):
        solve()
