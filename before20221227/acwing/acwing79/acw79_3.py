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

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda x: sys.stderr.write(f'{str(x)}\n')

MOD = 10 ** 9 + 7


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


def solve(n, k, s):
    s = list(map(int, s))
    cnt = Counter(s)
    mx = max(cnt.values())
    if mx >= k:
        return print(f"0\n{''.join(map(str, s))}")
    poses = [[] for _ in range(10)]
    for i, v in enumerate(s):
        poses[v].append(i)

    # 花x是否能搞出k个相同
    def calc(x):
        def f(i):
            cost = 0
            remain = k - cnt[i]
            for j in range(1, 10):
                if remain <= 0: break
                for p in i - j, i + j:
                    if 0 <= p <= 9:
                        c = min(cnt[p], remain)
                        cost += c * j
                        if cost > x: break
                        remain -= c
            return cost

        return any(f(i) <= x for i in range(10))

    mn = my_bisect_left(range(n * 10), True, key=calc)
    # DEBUG(mn)
    print(mn)

    def find(i):
        t = s[:]
        cost = 0
        remain = k - cnt[i]
        for j in range(1, 10):
            if remain <= 0:
                return ''.join(map(str, t))

            p = i + j
            if 0 <= p <= 9:
                ps = poses[p]
                c = min(cnt[p], remain)
                cost += c * j
                for x in range(c):
                    t[ps[x]] = i
                if cost > mn: break
                remain -= c
            p = i - j
            if 0 <= p <= 9:
                ps = poses[p][::-1]
                c = min(cnt[p], remain)
                cost += c * j
                for x in range(c):
                    t[ps[x]] = i
                if cost > mn: break
                remain -= c
        if remain <= 0:
            return ''.join(map(str, t))
        return 's'
    # for i in range(10):
    #     DEBUG((i,find(i)))
    print(min(find(i) for i in range(10)))


def main():
    n, k = RI()
    s, = RS()
    solve(n, k, s)


if __name__ == '__main__':
    # testcase 2个字段分别是input和output
    test_cases = (
        (
            """
6 5
898196
""",
            """
4
888188
"""
        ),
        (
            """
3 2
533
""",
            """
0
533
"""
        ),
        (
            """
10 6
0001112223
""",
            """
3
0000002223
"""
        ),
        (
            """
3 2
531
""",
            """
2
331
"""
        ),
    )
    if os.path.exists('test.test'):
        total_result = 'ok!'
        for i, (in_data, result) in enumerate(test_cases):
            result = result.strip()
            with io.StringIO(in_data.strip()) as buf_in:
                RI = lambda: map(int, buf_in.readline().split())
                RS = lambda: buf_in.readline().strip().split()
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
