# Problem: I. Photo Processing
# Contest: Codeforces - 2017-2018 ACM-ICPC, NEERC, Southern Subregional Contest (Online Mirror, ACM-ICPC Rules, Teams Preferred)
# URL: https://codeforces.com/problemset/problem/883/I
# Memory Limit: 256 MB
# Time Limit: 3000 ms

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
PROBLEM = """https://codeforces.com/problemset/problem/883/I

输入 n k(1≤k≤n≤3e5) 和长为 n 的数组 a(1≤a[i]≤1e9)。

把这 n 个数重新排列，然后分成若干个组，要求每组至少有 k 个数。
定义 diff(b) 表示序列 b 中最大值与最小值的差。
计算所有组的 diff 值的最大值 mx。
输出 mx 的最小值。
输入
5 2
50 110 130 40 120
输出 20

输入
4 1
2 3 4 1
输出 0
"""
"""https://codeforces.com/problemset/submission/883/205379777

排序后，二分答案。

贪心分组？看上去漏洞百出，不妨考虑 DP。

定义 f[i+1] 表示 a[0] 到 a[i] 能否满足要求。
初始值 f[0]=true，表示空数组满足要求。
先写一个 O(n^2) 的转移，也就是 f[i+1] = any(f[j])，这里 i-j+1 >= k 且 a[i]-a[j]<=mx，any(f[j]) 表示只要有一个 f[j] 是 true，f[i+1] 就是 true。
相当于，如果 a[0] 到 a[j-1] 满足要求，且 a[j] 到 a[i] 满足要求，那么 f[i+1] 就是 true。

如何优化？
设 f[i+1] 是从 f[j0] 转移过来的，这里 j0 是最大的满足 f[j0]=true 的下标。
那么 f[i+2] 可以从 >= j0 的下标转移过来，因为有 j0 的存在，且随着 i 的增大，j 能取到的最小值不会减少（因为 a[i]-a[j]<=mx），所以 j<j0 的 f[j] 就无需考虑了。
既然 j0 是单调递增的，利用这个性质就可以用双指针把 check 优化到 O(n)。"""

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


#   452    ms
def solve():
    n, k = RI()
    a = RILST()
    a.sort()

    def ok(x):
        f = [0] * (n + 1)
        f[0] = 1
        j = 0
        """双指针dp，令f[i]=0/1表示前i个数是否能合法拆分。
        当遍历到i时，i作为最后一段段尾，找到合法段首j，需要满足:
        ①f[j-1]==1
        ②且a[i]-a[j]<=x
        ③且i-j+1>=k。
        由于a是有序的，当i增加时，j必须增加才能满足②，因此：
        在长度>=k的情况下，右移j来满足②，前边丢弃的j不会对i+1后边的数产生贡献。
        然后继续右移找到第一个满足①的的j，前边丢弃的j不会都是f[j]=0，因此不会有贡献。
        最后判断长度即可。
        实现时，f右移一位令f[0]=1来简化代码
        """
        for i in range(k-1, n):
            while i - j + 1 >= k and a[i] - a[j] > x:
                j += 1
            while i - j + 1 >= k and f[j] == 0:
                j += 1
            if i - j + 1 >= k:
                f[i + 1] = 1
        return f[n] == 1
    print(lower_bound(0, a[-1] - a[0], ok))


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
