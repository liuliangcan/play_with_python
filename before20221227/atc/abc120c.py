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
PROBLEM = """https://atcoder.jp/contests/arc120/tasks/arc120_c

输入 n(≤2e5) 和两个长为 n 的数组 a b，元素范围在 [0,1e9]。
每次操作你可以选择 a 中的两个相邻数字，设 x=a[i], y=a[i+1]，更新 a[i]=y+1, a[i+1]=x-1。
输出把 a 变成 b 的最小操作次数，如果无法做到则输出 -1。

输入
3
3 1 4
6 2 0
输出 2

输入
3
1 1 1
1 1 2
输出 -1
https://atcoder.jp/contests/arc120/submissions/36718795

手玩一下可以发现，a[i] 左移 i 位就 +i，右移 i 位就 -i。
设 a[i] 最终和 b[j] 匹配，则有 a[i]+i-j=b[j]。
移项得 a[i]+i = b[j]+j。
设 a'[i] = a[i]+i，b'[i] = b[i]+i。
问题变成把 a' 通过邻项交换变成数组 b'，需要的最小操作次数。
这可以用树状数组解决，具体见代码。
"""

#   237    ms
def solve(n, a, b):
    for i in range(n):
        a[i] += i
        b[i] += i
    hs = defaultdict()
    hs.default_factory = hs.__len__
    for i,v in enumerate(b):
        b[i] = hs[v]
    for i,v in enumerate(a):
        if v not in hs:
            return print(-1)
        a[i] = hs[v]
    # print(a,b)
    from sortedcontainers import SortedList
    h = SortedList()
    ans = 0
    for v in a[::-1]:
        ans += h.bisect_left(v)
        h.add(v)
    print(ans)





def main(rs=None, ri=None):
    global RS, RI
    if rs:
        RS, RI = rs, ri
    n, = RI()
    a = RILST()
    b = RILST()
    solve(n, a, b)


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
