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


#    	 ms
def solve(n):
    a = 'abcde'
    if n <= 5:
        return print(a[n-1])
    x = 5
    while n > x:
        n -= x
        x *= 2
    if n == 0:
        return print('e')

    y = (n-1) // (x // 5)
    print(a[y])






def main():
    n, = RI()
    solve(n)


if __name__ == '__main__':
    # testcase 2个字段分别是input和output
    test_cases = (
        (
            """
1
""",
            """
a
"""
        ),
        (
            """
8
""",
            """
a
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
