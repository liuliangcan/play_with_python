# Problem: D2. Coffee and Coursework (Hard Version)
# Contest: Codeforces - Codeforces Round 540 (Div. 3)
# URL: https://codeforces.com/problemset/problem/1118/D2
# Memory Limit: 256 MB
# Time Limit: 2500 ms

import sys
import bisect
import random
import io, os
from bisect import *
from collections import *
from contextlib import redirect_stdout
from itertools import *
from array import *
from functools import lru_cache, reduce
from types import GeneratorType
from heapq import *
from math import sqrt, gcd, inf

if sys.version >= '3.8':  # ACW没有comb
    from math import comb

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')
# print = lambda d: sys.stdout.write(str(d) + "\n")  # 打开可以快写，但是无法使用print(*ans,sep=' ')这种语法

MOD = 10 ** 9 + 7
PROBLEM = """https://codeforces.com/problemset/problem/1118/D2

输入 n(1≤n≤2e5) (1≤m≤1e9) 和长为 n 的数组 a(1≤a[i]≤1e9)。

把这 n 个数重新排列，然后分成 x 个组。
每个组的第一个数不变，第二个数减一，第三个数减二，依此类推。
如果有数字减成负数，则从组中去掉。

要使所有数字之和至少为 m，x 最小是多少？
如果无法做到，输出 -1。
输入
5 8
2 3 1 1 2
输出
4

输入
7 10
1 3 4 2 1 4 2
输出
2

输入
5 15
5 5 5 5 5
输出
1

输入
5 16
5 5 5 5 5
输出
2

输入
5 26
5 5 5 5 5
输出
-1
"""
"""二分+贪心
首先想想最大能是几，显然每个数分一组，mx=sum(a)。
    - mx<m则永远无法到达m,返回-1
    - 否则一定可以>=m。而且可以每次变化1
题目问的是'最小''至少'，'至少'可以理解成构造为'最大'，那么题目就是'最小化最大值'。考虑二分。
显然分成n组得到的结果是最大的。分成1组是最小的。(这里由于1<=a[i],min(n,m)组即可)
如何进行最大构造呢，

优先用大的数字更优，放置方案为：a 倒序排，先把最大的 x 个数每个组放一个，然后剩下的 x 个最大的数每个组放一个，依此类推。
另一个启发思路是，很小的数字被减去的量也更小，比如 2 至多减去 2，所以把小的数字排在后面，整体减少的量更小。
"""


def lower_bound(lo: int, hi: int, key):
    """由于3.10才能用key参数，因此自己实现一个。
    :param lo: 二分的左边界(闭区间)
    :param hi: 二分的右边界(闭区间)
    :param key: key(mid)判断当前枚举的mid是否应该划分到右半部分。
    :return: 右半部分第一个位置。若不存在True则返回hi+1。
    虽然实现是开区间写法，但为了思考简单，接口以[左闭,右闭]方式放出。
    """
    lo -= 1  # 开区间(lo,hi)
    hi += 1
    while lo + 1 < hi:  # 区间不为空
        mid = (lo + hi) >> 1  # py不担心溢出，实测py自己不会优化除2，手动写右移
        if key(mid):  # is_right则右边界向里移动，目标区间剩余(lo,mid)
            hi = mid
        else:  # is_left则左边界向里移动，剩余(mid,hi)
            lo = mid
    return hi


#   155    ms
def solve():
    n, m = RI()
    a = RILST()
    if sum(a) < m:
        return print(-1)
    a.sort(reverse=True)

    def ok(x):
        s = 0
        i = 0
        d = 0
        while i < n:
            for _ in range(x):
                if i >= n: break
                p = a[i] - d
                if p <= 0:
                    i = n
                    break
                s += p
                if s >= m:
                    return True
                i += 1
            d += 1
        return False

    print(lower_bound(1, min(n,m), ok))






if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
