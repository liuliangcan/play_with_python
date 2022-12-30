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
def solve(n, a):
    h = []
    a = sorted(zip(a, range(n)))
    t = deque()
    ans = [-1] * n
    for v, idx in a:
        while t and a[t[0]] != v:
            heapq.heappush(h, -t.popleft())
        if h and -h[0] > idx:
            ans[idx] = -h[0] - idx - 1
        t.append(idx)

    print(' '.join(map(str, ans)))


def main():
    n, = RI()
    a = RILST()
    solve(n, a)


if __name__ == '__main__':
    # testcase 2个字段分别是input和output
    test_cases = (
        (
            """
6
10 8 5 3 50 45
""",
            """
2 1 0 -1 0 -1
"""
        ),
        (
            """
7
10 4 6 3 2 8 15
""",
            """
4 2 1 0 -1 -1 -1 
"""
        ),
        (
            """
5
10 3 1 10 11
""",
            """
1 0 -1 -1 -1 
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
