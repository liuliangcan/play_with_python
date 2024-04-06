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

# if not sys.version.startswith('3.5.3'):  # ACW没有comb
#     from math import comb

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')
# print = lambda d: sys.stdout.write(str(d) + "\n")  # 打开可以快写，但是无法使用print(*ans,sep=' ')这种语法,需要print(' '.join(map(str, p)))，确实会快。

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 右下左上
DIRS8 = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]  # →↘↓↙←↖↑↗
RANDOM = random.randrange(2 ** 62)
MOD = 10 ** 9 + 7
# MOD = 998244353
PROBLEM = """https://www.lanqiao.cn/problems/17161/learning/?contest_id=179
m进制下，钱珀瑙恩常数的第n位是几？
先计算目标位所在的数字v，是几位数。这可以一层一层尝试累加上去。
然后计算v在本层是第几个数（注意上取整），从而得出是整个的第几(k)个数。
那么v=basek(k,m)，即：在m进制下，第k个数是几？那就是十进制k转m进制
最后计算在v数字本身中的第几位
"""


def basek(v, k):
    ans = []
    while v:
        x, y = divmod(v, k)
        ans.append(y)
        v = x
    s = ''.join(map(str, ans))
    return s[::-1]


def decimal_to_base_k(decimal_num, base):
    digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = ''

    while decimal_num > 0:
        remainder = decimal_num % base
        result = digits[remainder] + result
        decimal_num //= base

    return result


def calc(n, m):
    i = 0
    while n - (m - 1) * (i + 1) * m ** i > 0:
        n = n - (m - 1) * (i + 1) * m ** i
        i += 1
    print(i, n)
    loc, seq = n % (i + 1), n // (i + 1)
    seq = seq if loc == 0 else seq + 1
    print(decimal_to_base_k(seq + pow(m, i) - 1, m)[loc - 1])


#       ms
def solve():
    n, m = RI()
    i = 1  # 第n位处在i位数上
    cnt = 0  # i位数之前共有多少个数位

    while cnt + (m ** i - m ** (i - 1)) * i < n:
        cnt += (m ** i - m ** (i - 1)) * i
        i += 1

    k = (n - cnt + i - 1) // i + (m ** (i - 1)) - 1  # 整体是第k个数
    a = basek(k, m)

    print(a[(n - cnt) % i - 1])



if __name__ == '__main__':
    t = 1
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
