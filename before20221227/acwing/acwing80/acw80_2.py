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

INF = 10**10
#    	 ms
def solve(a):
    s = str(a)
    n = len(s)
    if n & 1:
        s = '0' + s
    else:
        b = int('7' * (n // 2) + '4' * (n // 2))
        if a == b:
            return print(a)
        elif a > b:
            s = '0' * 2 + s
    n = len(s)
    # DEBUG((n,s))
    @lru_cache(None)
    def f(i, pre, is_limit):
        x = str(pre)
        c4 = x.count('4')
        c7 = x.count('7')
        if i == n:
            if c4 == c7:
                return pre
            else:
                return INF
        ans = INF
        if c4 < n // 2:
            if not is_limit:
                ans = min(ans, f(i + 1, pre * 10 + 4, False))
            else:
                if int(s[i]) <= 4:
                    ans = min(ans, f(i + 1, pre * 10 + 4, int(s[i]) == 4))
        if c7 <= n // 2:
            if not is_limit:
                ans = min(ans, f(i + 1, pre * 10 + 7, False))
            else:
                if int(s[i]) <= 7:
                    ans = min(ans, f(i + 1, pre * 10 + 7, int(s[i]) == 7))
        return ans

    print(f(0, 0, True))


def main():
    n, = RI()
    solve(n)


if __name__ == '__main__':
    # testcase 2个字段分别是input和output
    test_cases = (
        (
            """
4500
""",
            """
4747
"""
        ),
        (
            """
47
""",
            """
47
"""
        ),
        (
            """
1
""",
            """
47
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
