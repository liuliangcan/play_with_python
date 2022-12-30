import sys
from collections import *
from contextlib import redirect_stdout
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

MOD = 10 ** 9 + 7
PROBLEM = """https://atcoder.jp/contests/abc130/tasks/abc130_e

输入 n(≤2000) 和 m(≤2000)，长度分别为 n 和 m 的数组 a 和 b，元素范围 [1,1e5]。
从 a 和 b 中分别选出一个子序列（允许为空），要求这两个子序列相同。
输出有多少种不同的选法，模 1e9+7。
注意：选出的子序列不同，当且仅当下标不同（即使子序列的元素是相同的，也算不同）。
输入
2 2
1 3
3 1
输出 3
解释 注意空子序列也算

输入
2 2
1 1
1 1
输出 6
"""


#  2212 TLE   ms
def solve1(n, m, a, b):
    f = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:
                f[i][j] = f[i - 1][j - 1] + 1
            f[i][j] += (f[i - 1][j] + f[i][j - 1] - f[i - 1][j - 1])
            f[i][j] %= MOD
    print((f[-1][-1] + 1) % MOD)


#   1713   ms
def solve2(n, m, a, b):
    f = [0] * (m + 1)
    for i in range(1, n + 1):
        g = f[:]
        for j in range(1, m + 1):
            f[j] += f[j - 1] - g[j - 1] + (g[j - 1] + 1) * (a[i - 1] == b[j - 1])
            f[j] %= MOD

    print((f[-1] + 1) % MOD)


#  1708    ms
def solve(n, m, a, b):
    dp = [[0] * (m + 1) for _ in range(2)]
    for i in range(1, n + 1):
        g, f = dp[i & 1], dp[i & 1 ^ 1]
        for j in range(1, m + 1):
            f[j] = (g[j] + f[j - 1] - g[j - 1] + (g[j - 1] + 1) * (a[i - 1] == b[j - 1])) % MOD

    print((dp[n & 1 ^ 1][-1] + 1) % MOD)


def main(rs=None, ri=None):
    global RS, RI
    if rs:
        RS, RI = rs, ri
    n, m = RI()
    a = RILST()
    b = RILST()
    solve(n, m, a, b)


if __name__ == '__main__':
    # testcase 2个字段分别是input和output
    test_cases = (
        (
            """
2 2
1 3
3 1
""",
            """
3
"""
        ),
        (
            """
2 2
1 1
1 1
""",
            """
6
"""
        ),
    )
    if os.path.exists('test.test'):
        from atc.AtcLocalTest import AtcLocalTest

        AtcLocalTest(main, url=PROBLEM.strip().split('\n')[0].strip(), test_cases=test_cases, spider_switch=True).run()
    else:
        main()
