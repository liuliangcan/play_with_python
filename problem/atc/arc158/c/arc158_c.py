# Problem: C - All Pair Digit Sums
# Contest: AtCoder - AtCoder Regular Contest 158
# URL: https://atcoder.jp/contests/arc158/tasks/arc158_c
# Memory Limit: 1024 MB
# Time Limit: 4000 ms

import sys
import random
from types import GeneratorType
import bisect
import io, os
from bisect import *
from collections import *
from contextlib import redirect_stdout
from itertools import *
from array import *
from functools import lru_cache, reduce
from heapq import *
from math import sqrt, gcd, inf

if sys.version >= '3.8':  # ACW没有comb
    from math import comb

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')
# print = lambda d: sys.stdout.write(str(d) + "\n")  # 打开可以快写，但是无法使用print(*ans,sep=' ')这种语法,需要print(' '.join(map(str, p)))，确实会快。

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 右下左上
DIRS8 = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0),
         (-1, 1)]  # →↘↓↙←↖↑↗
RANDOM = random.randrange(2 ** 62)
MOD = 10 ** 9 + 7
# MOD = 998244353
PROBLEM = """https://atcoder.jp/contests/arc158/tasks/arc158_c

输入 n(1≤n≤2e5) 和长为 n 的数组 a(1≤a[i]≤1e15)。
定义 f(x) 为 x 的数位和。例如 f(123)=1+2+3=6。
输出所有 f(a[i]+a[j]) 的和，其中 i 取遍 0 到 n-1，j 取遍 0 到 n-1。
输入
2
53 28
输出 36

输入 
1
999999999999999
输出 135

输入
5
123 456 789 101 112
输出 321
"""
"""提示 1：f(x+y)=f(x)+f(y)-9*k(x,y)，其中 k(x,y) 是计算 x+y 时产生的进位次数。

提示 2：拆位计算，即：
1. 有多少 a[i]+a[j] 时，个位数发生了进位？也就是看 a[i]%10+a[j]%10 >= 10 是否成立。
把数组按照 a[i]%10 排序，然后用相向双指针统计。
2. 有多少 a[i]+a[j] 时，十位数发生了进位？也就是看 a[i]%100+a[j]%100 >= 100 是否成立。
把数组按照 a[i]%100 排序，然后用相向双指针统计。
3. 依此类推，直到 1000..0 > 2*max(a) 时停止。

提示 3：其实到这就说完了，这里补充下怎么化简 ∑_i ∑_j f(a[i])+f(a[j])
 ∑_i ∑_j f(a[i])+f(a[j])
=∑_i (n*f(a[i])+∑_j f(a[j]))
=(n*∑f(a[i])) + (n*∑f(a[j]))
=2n*∑f(a[i])

https://atcoder.jp/contests/arc158/submissions/44190713"""


#       ms
def solve():
    n, = RI()
    a = RILST()
    ds = carry = 0
    for v in a:
        ds += sum(map(int, str(v)))
    mx = max(a)
    pw = 10
    while pw <= mx * 2:
        a.sort(key=lambda x: x % pw)
        r = n - 1
        for l, v in enumerate(a):
            while r >= 0 and v % pw + a[r] % pw >= pw:
                r -= 1
            carry += n - r - 1

        pw *= 10
    print(2 * ds * n - carry * 9)


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
