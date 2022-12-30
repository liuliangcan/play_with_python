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
PROBLEM = """https://atcoder.jp/contests/abc203/tasks/abc203_d

输入 n k (1≤k≤n≤800) 和一个 n*n 的矩阵，元素范围 [0,1e9]。
定义 k*k 子矩阵的中位数为子矩阵的第 floor(k*k/2)+1 大的数。
输出中位数的最小值。
注：「第 x 大」中的 x 从 1 开始。
输入
3 2
1 7 0
5 8 11
10 4 2
输出 4

输入
3 3
1 2 3
4 5 6
7 8 9
输出 5
https://atcoder.jp/contests/abc203/submissions/36519551

二分答案。

猜测答案为 up，如果子矩阵内的 ≤ up 的数至少有 ceil(k*k/2) 个，那么答案可以 ≤ up。

这是满足单调性的，所以可以用二分。

用二维前缀和加速计算。
"""


class PreSum2d:
    # 二维前缀和(支持加法和异或)，只能离线使用，用n*m时间预处理，用O1查询子矩阵的和；op=0是加法，op=1是异或
    def __init__(self, g, op=0):
        m, n = len(g), len(g[0])
        self.op = op
        self.p = p = [[0] * (n + 1) for _ in range(m + 1)]
        if op == 0:
            for i in range(m):
                for j in range(n):
                    p[i + 1][j + 1] = p[i][j + 1] + p[i + 1][j] - p[i][j] + g[i][j]
        elif op == 1:
            for i in range(m):
                for j in range(n):
                    p[i + 1][j + 1] = p[i][j + 1] ^ p[i + 1][j] ^ p[i][j] ^ g[i][j]

    # O(1)时间查询闭区间左上(a,b),右下(c,d)矩形部分的数字和。
    def sum_square(self, a, b, c, d):
        if self.op == 0:
            return self.p[c + 1][d + 1] + self.p[a][b] - self.p[a][d + 1] - self.p[c + 1][b]
        elif self.op == 1:
            return self.p[c + 1][d + 1] ^ self.p[a][b] ^ self.p[a][d + 1] ^ self.p[c + 1][b]


def my_bisect_left(a, x, lo=None, hi=None, key=None):
    """
    由于3.10才能用key参数，因此自己实现一个。
    :param a: 需要二分的数据
    :param x: 查找的值
    :param lo: 左边界
    :param hi: 右边界(闭区间)
    :param key: 数组a中的值会依次执行key方法，
    :return: 第一个大于等于x的下标位置
    """
    if not lo:
        lo = 0
    if not hi:
        hi = len(a) - 1
    else:
        hi = min(hi, len(a) - 1)
    size = hi - lo + 1

    if not key:
        key = lambda _x: _x
    while size:
        half = size >> 1
        mid = lo + half
        if key(a[mid]) < x:
            lo = mid + 1
            size = size - half - 1
        else:
            size = half
    return lo


#   780   ms·
def solve1(n, k, g):
    def calc(up):
        s = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if g[i][j] <= up:
                    s[i][j] = 1
        ps = PreSum2d(s)
        for i in range(n - k + 1):
            for j in range(n - k + 1):
                if ps.sum_square(i, j, i + k - 1, j + k - 1) >= (k * k + 2 - 1) // 2:
                    return 1
        return 0

    print(my_bisect_left(range(10 ** 9 + 10), 1, key=calc))

"""二分
只要有一组子矩阵满足小于up的数目足够(>= (k * k + 2 - 1) // 2)，则这个值就是有效的，只需要向left二分。
"""
#   735   ms·
def solve(n, k, g):
    s = [[0] * n for _ in range(n)]

    def calc(up):
        for i in range(n):
            for j in range(n):
                s[i][j] = g[i][j] <= up

        ps = PreSum2d(s)
        for i in range(n - k + 1):
            for j in range(n - k + 1):
                if ps.sum_square(i, j, i + k - 1, j + k - 1) >= (k * k + 2 - 1) // 2:
                    return 1
        return 0

    print(my_bisect_left(range(10 ** 9 + 10), 1, key=calc))


def main(rs=None, ri=None):
    global RS, RI
    if rs:
        RS, RI = rs, ri
    n, k = RI()
    g = []
    for _ in range(n):
        g.append(RILST())
    solve(n, k, g)


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
