# Problem: E - MEX
# Contest: AtCoder - AtCoder Beginner Contest 308
# URL: https://atcoder.jp/contests/abc308/tasks/abc308_e
# Memory Limit: 1024 MB
# Time Limit: 2000 ms

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
PROBLEM = """
https://atcoder.jp/contests/abc308/tasks/abc308_e

输入 n(3≤n≤2e5) 和长为 n 的数组 a(0≤a[i]≤2)，以及长为 n 的字符串，仅包含 'M' 'E' 'X'。
遍历所有满足 i<j<k 且 s[i]=M 且 s[j]=E 且 s[k]=X 的下标三元组 (i,j,k)，累加 mex(a[i],a[j],a[k]) 的值，输出这个累加值。
注：mex(a[i],a[j],a[k]) 表示不在 a[i],a[j],a[k] 中的最小非负整数。
输入
4
1 1 0 2
MEEX
输出 3

输入
3
0 0 0
XXX
输出 0

输入
15
1 1 2 0 0 2 0 2 0 0 0 0 0 2 2
EXMMXXXEMEXEXMM
输出 13
给出长为n的数列a，仅包含012
给出长为n的字符串s，仅包含'm''e''x'。
找到所有s中的mex三元组下标，对应的a中的三个数组成的集合，求mex，最后sum。
"""
"""由于三元组只含012因此一定求mex可以暴力最多操作4次。
mex一定从me转移而来才有效，me一定从m转移而来才有效。
而这些字母对应数字是有限的，可以用哈希表计数即可。
"""
"""方法一：前后缀分解

枚举中间的 j。我们需要知道左边满足 s[i]=M 的 0/1/2 的个数；右边满足 s[k]=X 的 0/1/2 的个数。
这可以预处理出来。
当 s[j]=E 时，枚举 j 左边的 0/1/2 和 j 右边的 0/1/2 的 9 种组合，再算上 a[j]，得到 mex。
例如 a[j]=1，左边有 5 个 1，右边有 3 个 0，那么 mex(1,1,0)=2，对答案的贡献是 5*3=15 个 mex，也就是 30。

https://atcoder.jp/contests/abc308/submissions/45101686 

方法二：状态机 DP

定义 f0[0/1/2] 表示当前统计的满足 s[i]=M 的 0/1/2 的个数。
定义 f1[1/2/3/4/5/6] 表示当前统计的满足 a[i]=M 且 a[j]=E 的 a[i] 和 a[j] 组成的集合（二进制表示）的个数，例如 f1[5] 表示集合 {0,2} 的个数。
遍历到 s[k]=X 时，枚举 mask=1/2/3/4/5/6，把答案加上 mex(mask 和 a[k] 组成的集合) * f1[mask]

https://atcoder.jp/contests/abc308/submissions/45102151"""


def mex(s):
    for i in count(0):
        if i not in s:
            return i


#  374     ms
def solve():
    n, = RI()
    a = RILST()
    s, = RS()
    ans = 0
    m, me, x = Counter(), Counter(), Counter()
    i = 0
    for x, c in zip(a, s):
        if c == 'M':
            m[x] += 1
        elif c == 'E':
            for k, v in m.items():
                me[(k, x)] += v
        else:
            for k, v in me.items():
                s = set(k)
                s.add(x)

                ans += mex(s) * v
        i += 1
    print(ans)



#   187    ms
def solve3():
    n, = RI()
    a = RILST()
    s, = RS()
    ans = 0

    def mex(s):
        res = 0
        while s >> res & 1:
            res += 1
        return res

    m, e = [0] * 8, [0] * 8
    for c, v in zip(s, a):
        if c == 'M':
            m[1 << v] += 1
        elif c == 'E':
            for k, cc in enumerate(m):
                e[k | (1 << v)] += cc
        else:
            for k, cc in enumerate(e):
                ans += mex(k | (1 << v)) * cc
    print(ans)


#   186    ms
def solve2():
    n, = RI()
    a = RILST()
    s, = RS()
    ans = 0

    def mex(s):
        res = 0
        while s >> res & 1:
            res += 1
        return res

    m, e, x = Counter(), Counter(), Counter()
    for c, v in zip(s, a):
        if c == 'M':
            m[1 << v] += 1
        elif c == 'E':
            for k, cc in m.items():
                e[k | (1 << v)] += cc
        else:
            for k, cc in e.items():
                ans += mex(k | (1 << v)) * cc
    print(ans)


#   283    ms
def solve1():
    n, = RI()
    a = RILST()
    s, = RS()
    ans = 0
    m, e, x = Counter(), Counter(), Counter()
    for c, v in zip(s, a):
        if c == 'M':
            m[v] += 1
        elif c == 'E':
            for k, cc in m.items():
                p = {k, v}
                e[''.join(map(str, sorted(p)))] += cc
        else:
            for k, cc in e.items():
                p = {int(c) for c in k} | {v}
                ans += mex(p) * cc
    print(ans)

if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
