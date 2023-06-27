# Problem: D. Changing Array
# Contest: Codeforces - Mail.Ru Cup 2018 Round 1
# URL: https://codeforces.com/problemset/problem/1054/D
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
PROBLEM = """https://codeforces.com/problemset/problem/1054/D

输入正整数 n(≤2e5) k(≤30) 和长为 n 的数组 a(0≤a[i]≤pow(2,k)-1)。

设 mask = (1<<k)-1，每次操作你可以把任意 a[i] 修改为 a[i] XOR mask，你可以操作任意次（包括 0 次）。
修改后，最多有多少个 a 的非空连续子数组，其异或和不等于 0？
输入
3 2
1 3 0
输出 5

输入
6 3
1 4 4 7 3 4
输出 19
"""
"""正难则反，异或前缀和，最后统一计数
1. 记a的前缀和s(s[0]补0)。s[i+1]=s[i]^a[i]。那么题目转化成要求s中的数对不同的尽量多。正难则反，即s中相同的数对尽量少。计算最小的数对即可。
    数对总数是C(n+1,2)，注意在前缀和上选数对，共n+1个数。
2. 对于a的某个前缀a[0:i],如果其中修改了偶数次，s[i]不变，因为相当于总体异或了偶数次mask,自己就抵消了；如果修改了奇数次，s[i]^=mask。
3. 对于每个s[i],他们之间是互相独立的，即修改前边某个数，s[i]变了，但到s[i]这位时依然可以自己变一次。
4. 同样可以推出，实际上s里的每一位可以看做s[i]或s[i]^mask，且这俩是可以互相转换的（即使算了个s[i]也等于s[i]^mask）,因此他们俩计数应该计到一起。
5. 为了方便，我们记到min(s[i],s[i]^mask)。
6. 统计完所有的计数，假设v的次数是x次，那么v能产生的数对是C(x,2)。为了让相同数对变少，那么把v拆两半，即一半v，一半v^mask。他们产生的相同数对就是C(x//2,2)+C(x-x//2,2)。
7. 减去所有相同数对即可。
"""

#       ms
def solve():
    n, k = RI()
    a = RILST()
    mask = (1 << k) - 1
    s = 0
    cnt = Counter([0])
    for v in a:
        s ^= v
        cnt[min(s, s ^ mask)] += 1

    def c2(x):
        return (x - 1) * x // 2

    ans = c2(n+1)
    for v in cnt.values():
        ans -= c2(v // 2) + c2(v - v // 2)
    print(ans)


if __name__ == '__main__':
    solve()
