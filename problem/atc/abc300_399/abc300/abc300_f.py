# Problem: F - More Holidays
# Contest: AtCoder - UNIQUE VISION Programming Contest 2023 Spring(AtCoder Beginner Contest 300)
# URL: https://atcoder.jp/contests/abc300/tasks/abc300_f
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
PROBLEM = """https://atcoder.jp/contests/abc300/tasks/abc300_f

输入 n(1≤n≤3e5) m(1≤m≤1e9) k 和长为 n 的字符串 s，只包含小写字母 'o' 和 'x'。
保证至少有一个 'x'，保证 1≤k≤s.count('x')*m。

将 s 重复 m 次，得到字符串 t。例如 "abc" 重复 3 次得到 "abcabcabc"。
请你修改 t 中的恰好 k 个 'x'。修改后，输出 t 中最长连续 'o' 的长度。
输入
10 1 2
ooxxooooox
输出 9

输入
5 3 4
oxxox
输出 8

输入
30 1000000000 9982443530
oxoxooxoxoxooxoxooxxxoxxxooxox
输出 19964887064
"""
"""先把中间能完整移除的段算出来a,b=divmod(k,cnt)
然后考虑两端的段怎么移除，一定是移除中间，但这两段实际上可以承载<2*cnt个，所以要尝试两种情况
"""

"""写了很多 if-else？
实际上有一种写法，完全不需要分类讨论！

设 pos 为所有 x 的下标列表（下标从 0 开始）。
设 pos 的长度为 cntX。

提示 1：把前 k 个 x 修改成 o，答案是多少？
min(k/cntX*n + pos[k%cntX], n*m)

提示 2：把前 2~k+1 个 x 修改成 o，答案是多少？
可以先算出「修改前 k+1 个 x」的答案，再减去「第一个 x 的下标 +1」。
把上面公式中的 k 替换成 k+1 就是「修改前 k+1 个 x」的答案。

依此类推，一直枚举到最后一个 x。

https://atcoder.jp/contests/abc300/submissions/44909568"""


#    142    ms
def solve():
    n, m, k = RI()
    s, = RS()
    c = s.count('x')
    pos = [i for i, v in enumerate(s) if v == 'x']
    a, b = divmod(k, c)
    ans = min(n * m, a * n + pos[b])
    for v in pos:
        k += 1
        ans = max(ans, min(k // c * n + pos[k % c], n * m) - v - 1)
    print(ans)


#    219    ms
def solve1():
    n, m, k = RI()
    s, = RS()
    c = s.count('x')
    if k == c * m:
        return print(n * m)

    def get(s, k):  # 从s中删除k个x，最多得到最长连续o是多少
        if k >= s.count('x'): return len(s)
        pos = [-1] + [i for i, v in enumerate(s) if v == 'x'] + [len(s)]
        ans = k
        q = deque()
        for v in pos:
            q.append(v)
            if len(q) > k + 1:
                ans = max(ans, v - q.popleft() - 1)
        return ans

    if m == 1:
        return print(get(s, k))

    ss = s + s
    a, b = divmod(k, c)  # 能完整得到a段，余b个可以修改

    ans = get(ss, k)
    if m - a >= 2:  # 段数多了两段，放到这a段两段
        ans = max(ans, a * n + get(ss, b))
    if a and m - a + 1 >= 2:  # 尝试挪一段出来，用以移除两端的
        ans = max(ans, (a - 1) * n + get(ss, b + c))
    print(ans)


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
