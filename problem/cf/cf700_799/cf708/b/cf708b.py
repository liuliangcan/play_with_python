# Problem: B. Recover the String
# Contest: Codeforces - AIM Tech Round 3 (Div. 1)
# URL: https://codeforces.com/problemset/problem/708/B
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
PROBLEM = """https://codeforces.com/problemset/problem/708/B

对于 01 字符串 s，定义 f(x,y) 表示子序列 [x,y] 在 s 中的出现次数。
输入 f(0,0), f(0,1), f(1,0) 和 f(1,1)，范围在 [0,1e9]。
请构造任意一个满足输入的非空字符串 s。
如果不存在，输出 Impossible。
注：子序列是从 s 中删除某些元素得到的。

可能是道易错题
输入 1 2 3 4
输出 Impossible

输入 1 2 2 1
输出 0110
"""
"""
0的个数是zero，则f(0,0)= zero*(zero-1)/2,这里可以考虑等差数列求和或者C(zero,2)
1同理。
则可以通过求根公式先求出0和1的个数，同时确定总长度；注意检查根应该是整数且>=0；枚举求根公式里的2X2种情况(wa case12，因为如果00是0，可以有1/0个0)。
总长度s,那么同理sum(f)应当=C(s,2)，检查。
考虑f(01)和f(10)是否合法：若0全在1前边，则f(01)=zero*one,f(10)=0；交界的01换位置，他们变化是+-1,连续的，那么这两个值可以取所有值都合法。
那么01、10的个数就任意了，考虑构造一个形如111000111的序列(即0都在中间连续)，这种情况下f(0,1)=zero*back1，
那么设back1,mod = divmod(f(0,1),zero);
显然back1就是后一段1的个数，尝试补齐剩余mod个01，只需把zero里第一个0向前挪mod位，就会导致mod个1在这个0后边，恰好可以多mod个01。

特判zero=0 or one=0的情况。
特判case4:0 0 0 0 显然长度为1即可。
"""

#   108    ms
def solve():
    f = RILST()
    """x*(x-1)/2=f[0]
    x^2 - x -2f[0] = 0
    x = (1 + sqrt(1+8f[0]))/2
    """
    if sum(f) == 0:
        return print('0')
    # zero = int((1 + (1 + 8 * f[0]) ** 0.5) / 2)
    # one = int((1 + (1 + 8 * f[3]) ** 0.5) / 2)
    for zero in int((1 + (1 + 8 * f[0]) ** 0.5) / 2), int((1 - (1 + 8 * f[0]) ** 0.5) / 2):
        for one in int((1 + (1 + 8 * f[3]) ** 0.5) / 2), int((1 - (1 + 8 * f[3]) ** 0.5) / 2):
            # print(zero, one)
            if zero < 0 or one < 0:
                continue
            if zero * (zero - 1) // 2 != f[0] or one * (one - 1) // 2 != f[3] or (zero + one) * (
                    zero + one - 1) // 2 != sum(f):
                continue

            if zero == 0:
                return print('1' * one)
            if one == 0:
                return print('0' * zero)
            back1, mod = divmod(f[1], zero)
            front1 = one - back1
            zs = [0] * zero
            front = [1] * front1
            back = [1] * back1
            if mod:
                front[-1] = 0
                zs[mod - 1] = 1
            return print(''.join(map(str, front + zs + back)))

    print('Impossible')


if __name__ == '__main__':
    solve()
