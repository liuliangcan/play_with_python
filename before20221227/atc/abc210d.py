import sys
from collections import *
from contextlib import redirect_stdout
from itertools import *
from math import sqrt, gcd, inf
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
PROBLEM = """https://atcoder.jp/contests/abc210/tasks/abc210_d

输入 n m (2≤n,m≤1000) c(≤1e9) 和一个 n 行 m 列的矩阵 a，元素范围 [1,1e9]。
对于两个不同位置 (i,j) 和 (i',j')，输出 a[i][j] + a[i'][j'] + c*(|i-i'|+|j-j'|) 的最小值。
输入
3 4 2
1 7 7 9
9 6 3 7
7 8 6 4
输出 10

输入
3 3 1000000000
1000000 1000000 1
1000000 1000000 1000000
1 1000000 1000000
输出 1001000001
https://atcoder.jp/contests/abc210/submissions/36539833

逐行遍历矩阵。

把式子拆开：

1. 如果 (i',j') 在 (i,j) 的正左/左上/正上，那么相当于求
a[i][j]+c*(i+j) + min{a[i'][j']-c*(i'+j')} 的最小值。
后面 min 的内容可以用一个 pre_min 数组维护。
正左可以用 pre_min[j-1]，左上和正上是 pre_min[j]。
代码实现时，为了避免出现 -1 下标，pre_min 的下标改成从 1 开始。

2. 如果 (i',j') 在 (i,j) 的右上，那么相当于求
a[i][j]+c*(i-j) + min{a[i'][j']-c*(i'-j')} 的最小值。
后面 min 的内容可以用一个 suf_min 数组维护。注意这个需要倒着遍历矩阵的行。

根据对称性，我们只需要考虑这两种情况。
"""


#      ms
def solve(n, m, c, a):
    pre = [inf] * (m + 1)
    suf = [inf] * (m + 1)
    ans = inf
    for i in range(n):
        for j in range(m):
            # DEBUG(i,j)
            ans = min(ans, a[i][j] + c * (i + j) + pre[j],a[i][j] + c * (i + j) + pre[j + 1])
            pre[j + 1] = min(pre[j + 1], pre[j], a[i][j] - c * (i + j))
        for j in range(m - 1, -1, -1):
            ans = min(ans, a[i][j] + c * (i - j) + suf[j])
            suf[j] = min(suf[j], suf[j + 1], a[i][j] - c * (i - j))

    print(ans)


def main(rs=None, ri=None):
    global RS, RI
    if rs:
        RS, RI = rs, ri
    n, m, c = RI()
    g = []
    for _ in range(n):
        g.append(RILST())
    solve(n, m, c, g)


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
