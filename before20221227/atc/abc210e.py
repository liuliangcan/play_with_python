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

MOD = 10 ** 9 + 7
# 当爬虫开关为True时，会在线爬case，main里设置的case会被覆盖不生效；如果要用本地case需要设置False;
# 爬取地址是PROBLEM第一行
SPIDER_SWITCH = True
PROBLEM = """https://atcoder.jp/contests/abc210/tasks/abc210_e

输入 n(≤1e9) 和 m(≤1e5)，表示一个 n 个点，0 条边的图（节点编号从 0 开始），以及 m 个操作。
每个操作输入两个数 a(1≤a≤n-1) 和 c(≤1e9)，表示你可以花费 c，任意选择一个 [0,n-1] 内的数字 x，把 x 和 (x+a)%n 连边。
这 m 个操作，每个都可以执行任意多次，可以按任意顺序执行。
输出让图连通需要的最小花费。
如果无法做到，输出 -1。
输入
4 2
2 3
3 5
输出 11

输入
6 1
3 4
输出 -1
https://atcoder.jp/contests/abc210/submissions/36506266

根据 Kruskal，按照 c 从小到大排序，对于每个操作，执行的次数等于执行前后连通块的数量之差。

由于每个操作需要尽可能多地执行，手玩一下可以发现，执行后的连通块数量等于 gcd(n, a0, a1, ..., ai)。

详细证明见右。https://atcoder.jp/contests/abc210/editorial/2307

如果最后 gcd > 1，则输出 -1。
"""


#      ms
def solve(n, m, ops):
    ops.sort(key=lambda x: x[1])
    ans = 0
    for a, c in ops:
        g = gcd(n, a)
        ans += (n - g) * c
        n = g
        if n == 1:
            break
    if n > 1:
        return print(-1)

    print(ans)


def main():
    n, m = RI()
    ops = []
    for _ in range(m):
        ops.append(RILST())
    solve(n, m, ops)


if __name__ == '__main__':
    # testcase 2个字段分别是input和output
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

    if os.path.exists('test.test'):
        if SPIDER_SWITCH:
            from atc.AtcCaseSpider import AtcCaseSpider
            test_cases = AtcCaseSpider(PROBLEM.strip().split()[0].strip()).cases()
        total_result = 'ok!'
        for i, (in_data, result) in enumerate(test_cases):
            result = result.strip()
            with io.StringIO(in_data.strip()) as buf_in:
                RI = lambda: map(int, buf_in.readline().split())
                RS = lambda: map(bytes.decode, buf_in.readline().strip().split())
                with io.StringIO() as buf_out, redirect_stdout(buf_out):
                    main()
                    output = buf_out.getvalue().strip()
                if output == result:
                    print(f'case{i}, result={result}, output={output}, ---ok!')
                else:
                    print(f'case{i}, result={result}, output={output}, ---WA!---WA!---WA!')
                    total_result = '---WA!---WA!---WA!'
        print('\n', total_result)
    else:
        main()
