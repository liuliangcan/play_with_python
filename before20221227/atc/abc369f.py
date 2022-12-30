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

MOD = 998244353
PROBLEM = """https://atcoder.jp/contests/abc269/tasks/abc269_f

输入 n m (≤1e9) q(≤2e5)。表示一个 n 行 m 列的矩阵。
第 i 行第 j 列的元素为 (i-1)*m+j，但是如果 i+j 是奇数，则该元素为 0。
输入 q 个询问，每个询问输入 r1 r2 c1 c2。
对每个询问，输出所有在第 r1~r2 行 c1~c2 列的元素之和，模 998244353。
输入
5 4
6
1 3 2 4
1 5 1 1
5 5 1 4
4 4 2 2
5 5 4 4
1 5 1 4
输出
28
27
36
14
0
104

---
1 0 3 0 
0 6 0 8
9 0 11 0
0 14 0 16
17 0 19 0
"""

inv2 = pow(2, MOD - 2, MOD)


#   723     ms
def solve(n, m, r1, r2, c1, c2):
    def sum_row_pre(r, c):  # 计算第r行前c个数的和（从0计数）
        # 不看0,项都是间隔2,因此求出第一项最后一项和高计算即可。
        h = (c + 2 - (r & 1)) // 2  # 等差数列长度,注意计算长度这里由于利用整除2，不要用逆元
        if not h:
            return 0
        a = r * m % MOD + (r & 1) + 1  # 等差数列第一项
        b = a + 2 * (h - 1)  # 等差数列最后一项
        return (a + b) * h * inv2 % MOD

    def f(r, c):  # 计算前r行前c个数的和（从0计数）
        # 发现奇数行的和是等差数列；偶数项也是，分别计算即可。
        # 偶数行0,2,4..
        h = r // 2 + 1
        a = sum_row_pre(0, c)  # 偶数行的第一行
        b = sum_row_pre(r if r & 1 == 0 else r - 1, c)  # 偶数行的最后一行
        ans = (a + b) * h * inv2 % MOD
        # 奇数行1,3,5...
        h = (r + 1) // 2
        a = sum_row_pre(1, c)
        b = sum_row_pre(r if r & 1 else r - 1, c)
        ans += (a + b) * h * inv2 % MOD
        return ans % MOD

    print((f(r2, c2) + f(r1 - 1, c1 - 1) - f(r1 - 1, c2) - f(r2, c1 - 1)) % MOD)


def main(rs=None, ri=None):
    global RS, RI
    if rs:
        RS, RI = rs, ri
    n, m = RI()
    q, = RI()
    for _ in range(q):
        r1, r2, c1, c2 = RI()
        solve(n, m, r1 - 1, r2 - 1, c1 - 1, c2 - 1)


if __name__ == '__main__':
    if os.path.exists('test.test'):
        inner_editor_case = False  # 使用编辑器里硬编码的数据测试，即下边的test_cases；默认False，即测试所有用例，如果本地不存在就在线爬

        # testcase 2个字段分别是input和output；仅当 spider_switch=False时，这里才生效，否则会在线爬
        test_cases = (
            (
                """
   4
1 1 2 3
1 2 3 3
    """,
                """
    Yes
3 3 1 2
    """
            ),
        )
        from atc.AtcLocalTest import AtcLocalTest

        if inner_editor_case:
            AtcLocalTest(main, url=PROBLEM.strip().split('\n')[0].strip(), test_cases=test_cases,
                         spider_switch=False).run()
        else:
            choose_case = {}  # 默认空，如果不为空则只会测这几个指定的case
            # choose_case = {'case03','case04'}
            AtcLocalTest(main, url=PROBLEM.strip().split('\n')[0].strip(), test_cases=test_cases,
                         choose_case=choose_case,
                         spider_switch=True).run()
    else:
        main()
