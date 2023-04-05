# Problem: F - Simultaneous Swap
# Contest: AtCoder - AtCoder Beginner Contest 296
# URL: https://atcoder.jp/contests/abc296/tasks/abc296_f
# Memory Limit: 1024 MB
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
PROBLEM = """https://atcoder.jp/contests/abc296/tasks/abc296_f
给你N(3<=N<=2e5)，和两个长度为n的数组a,b。
你可以做如下操作任意次或不做：
选下标j!=i!=k，同时交换：在a中交换a[i]a[j].再b中交换b[i]b[k]
若可以使a完全等于b输出Yes，否则输出No。
"""
"""群里大佬说正解是逆序对，我没看懂，直接找性质做的。没想到直接交就TLE了，优化了一下就过了
这里吐槽一下for x in set:break 是会TLE的，看来虽然提前break但没用，依然是O(n)。
1
2
首先a和b的元素对应数量必须相同，用sorted(a) != sorted(b)特判。
手玩发现，如果有1个元素出现两次，那么按照case1的方法交换，一定可以使另外一个位置相同，此时必Yes。
然后是模拟验证所有元素只出现一次的情况：
使第一个位置元素相同，只需找到一个还没处理的数字，找到它在ab分别的位置，把这个元素换过来。
然后依次处理第2\3\4…个位置。如果遇到本来就相同就不用动。
直到处理完倒数第三个位置，这时后两个位置如果不同则不行，如果完全相同才行，因为他们无法做出有用的交换了。
逆序对做法：如果ab的逆序对数奇偶性相同，则可以交换；否则不能交换。
当然前几个特判依然需要。
————————————————
版权声明：本文为CSDN博主「七水shuliang」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/liuliangcan/article/details/129972406"""

#       ms
def solve():
    n, = RI()
    a = RILST()
    b = RILST()

    if a == b:
        return print('Yes')
    if sorted(a) != sorted(b):
        return print('No')
    if len(set(a)) < n:
        return print('Yes')
    posa = {v: i for i, v in enumerate(a)}
    posb = {v: i for i, v in enumerate(b)}
    left = set(a)

    def get(x, y):
        s = set()
        ans = 0
        nonlocal left
        for _ in range(3):
            p = left.pop()
            if x != p != y:
                ans = p
            s.add(p)
        left |= s
        return ans

    for i in range(n - 2):
        if a[i] == b[i]:
            left.remove(a[i])
        else:
            v = get(a[i], b[i])
            pa = posa[v]
            pb = posb[v]
            left.remove(v)
            posa[a[i]] = pa
            posb[b[i]] = pb
            a[pa] = a[i]
            b[pb] = b[i]
    if a[-1] == b[-1] and a[-2] == b[-2]:
        return print('Yes')
    print('No')


if __name__ == '__main__':
    solve()
