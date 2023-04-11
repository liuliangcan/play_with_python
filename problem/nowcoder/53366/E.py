# Problem: 小d的博弈
# Contest: NowCoder
# URL: https://ac.nowcoder.com/acm/contest/53366/E
# Memory Limit: 524288 MB
# Time Limit: 2000 ms

import sys
from functools import lru_cache

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')

MOD = 10 ** 9 + 7
PROBLEM = """
"""


@lru_cache(None)
def dfs(m, n):
    if m <= 2 and n <= 2:
        return False
    if m <= 2 or n <= 2:
        return True
    for i in range(1, (m + 1) // 2):
        if not dfs(i, n):
            return True
    for j in range(1, (n + 1) // 2):
        if not dfs(m, j):
            return True
    return False


#     603  ms
def solve1():
    n, m = RI()
    y = x = 0
    while n > 2:
        n = (n - 1) // 2
        x += 1
    while m > 2:
        m = (m - 1) // 2
        y += 1
    if x != y:
        print('Alice')
    else:
        print('Bob')


#   573    ms
def solve():
    n, m = RI()

    if (n + 1).bit_length() != (m + 1).bit_length():
        print('Alice')
    else:
        print('Bob')


if __name__ == '__main__':
    t, = RI()
    for _ in range(t):
        solve()
    # for i in range(1, 40):
    #     for j in range(1, 40):
    #         print('X' if dfs(i, j) else 'O', end=' ')
    #     print()
