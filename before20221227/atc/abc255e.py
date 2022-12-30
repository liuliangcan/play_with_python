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
"""https://atcoder.jp/contests/abc255/tasks/abc255_e

输入 n (2≤n≤1e5) 和 m(≤10)，长为 n-1 的数组 s 和长为 m 的严格递增数组 x，元素值范围在 [-1e9,1e9]。
数组 x 中的元素叫做幸运数。
对于一个长为 n 的序列 a，如果所有相邻元素满足 a[i]+a[i+1]=s[i]，则称为一个好序列。
输出好序列中最多能有多少个数是幸运数（重复数字也算，见样例）。
输入
9 2
2 3 3 4 -4 -7 -4 -1
-1 5
输出 4
解释 a=[3,−1,4,−1,5,−9,2,−6,5]

输入
20 10
-183260318 206417795 409343217 238245886 138964265 -415224774 -499400499 -313180261 283784093 498751662 668946791 965735441 382033304 177367159 31017484 27914238 757966050 878978971 73210901
-470019195 -379631053 -287722161 -231146414 -84796739 328710269 355719851 416979387 431167199 498905398
输出 8
https://www.luogu.com.cn/blog/endlesscheng/solution-at-abc255-e
a[0] = x[j]
a[1] = s[0] - a[0]
a[2] = s[1] - a[1] = s[1] - s[0] + a[0]
a[3] = s[2] - a[2] = s[2] - s[1] + s[0] - a[0]
移项 -->
a[0] = s[0] - s[1] + s[2] - s[3] +..+(-1)**i*s[i] - (-1)**i*a[i+1]
显然确定了一个数，整个数组都被定下来了。也就是说知道任意数，其它数都可以计算。
因此这里我们尝试推到出一个可以递推的公式，方便跟着for向后累计，即用用任意a[i+1]计算a[0]，计数a[0]相同结果出现的次数。
这里的意义是：
    当a[0]出现2次同样的数v时，代表通过a[i]和a[j]都计算出同样的a[0]=v，翻过来显然使用这个值a[0]=v可以计算出a[i] a[j]两个幸运数字。
    多个计数同理。
注意这里是遍历s[0:n]推a[0:n+1]，因此每个x[j]作为a[0]的情况要进入初始化。
"""


#   407  	 ms
def solve(n, m, s, x):
    cnt = Counter(x)
    ss = 0
    p = 1
    for i, v in enumerate(s):
        ss += p * v
        for y in x:
            z = ss - y * p
            cnt[z] += 1
        p *= -1
    print(cnt.most_common(1)[0][1])


if __name__ == '__main__':
    n, m = RI()
    s = RILST()
    x = RILST()

    solve(n, m, s, x)
