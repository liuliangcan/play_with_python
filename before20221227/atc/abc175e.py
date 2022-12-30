import sys
from collections import *
from contextlib import redirect_stdout
from itertools import *
from math import sqrt, gcd
from array import *
from functools import lru_cache
import heapq
import bisect
import random
import io, os
from bisect import *

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')

MOD = 10 ** 9 + 7
PROBLEM = """https://atcoder.jp/contests/abc175/tasks/abc175_e

输入 n m (1≤n,m≤3000) k(≤min(2e5,r*c))，表示一个 n*m 的网格，和网格中的 k 个物品。
接下来 k 行，每行三个数 x y v(≤1e9) 表示物品的行号、列号和价值（行列号从 1 开始）。
每个网格至多有一个物品。

你从 (1,1) 出发走到 (n,m)，每步只能向下或向右。
经过物品时，你可以选或不选，且每行至多可以选三个物品。
输出你选到的物品的价值和的最大值。
输入
2 2 3
1 1 3
2 1 4
1 2 5
输出 8

输入
2 5 5
1 1 3
2 4 20
1 2 1
1 3 4
1 4 2
输出 29
"""
"""
定义f[i][j][0~3]为到达f[i][j]时，本行选了0~3个物品时的获得最大价值
初始:
    f[0][0][0] = 0
    f[0][0][1] = g[0][0]
    f[0][j][k] = f[0][j-1][k-1]+g[0][j]
    f[i][j][0] = max(f[i-1][j])  # 不选的话从上边来即可，从左边来不会比上边更好(因为一定是从上边更左下来,且不多选)
    f[i][j][1] = max(f[i-1][j])+g[i][j]
    f[i][j][k] = max(f[j - 1][k], f[j - 1][k - 1] + g[i][j], f[j][0] + g[i][j])
"""


#      ms
def solve(n, m, k, vs):
    dp = [[[0] * 4 for _ in range(m)] for _ in range(2)]
    f, g = dp
    f[0][1] = vs.get((0, 0), 0)  # 第一个位置选
    for j in range(1, m):
        for k in range(1, 4):
            f[j][k] = max(f[j - 1][k], f[j - 1][k - 1] + vs.get((0, j), 0))
    # DEBUG(f)
    for i in range(1, n):
        f, g = g, f
        f[0][0] = max(g[0])  # 第一个位置不选，
        f[0][1] = f[0][0] + vs.get((i, 0), 0)  # 第一个位置选
        for j in range(1, m):
            f[j][0] = max(g[j])  # 不选
            p = vs.get((i, j), 0)
            for k in range(1, 4):
                f[j][k] = max(f[j - 1][k], f[j - 1][k - 1] + p, f[j][0] + p)  # 不选、选+左边、选+上边

    # DEBUG(dp)
    print(max(f[-1]))


def main(rs=None, ri=None):
    global RS, RI
    if rs:
        RS, RI = rs, ri
    n, m, k = RI()
    vs = {}
    for _ in range(k):
        x, y, v = RI()
        vs[x - 1, y - 1] = v
    solve(n, m, k, vs)


if __name__ == '__main__':
    if os.path.exists('test.test'):
        # testcase 2个字段分别是input和output；仅当 spider_switch=False时，这里才生效，否则会在线爬
        test_cases = (
            (
                """
    4 2
    2 3
    3 5
    """,
                """
    11
    """
            ),
            (
                """
    6 1
    3 4
    """,
                """
    -1
    """
            ),
        )
        from atc.AtcLocalTest import AtcLocalTest

        AtcLocalTest(main, url=PROBLEM.strip().split('\n')[0].strip(), test_cases=test_cases, spider_switch=True).run()
    else:
        main()
