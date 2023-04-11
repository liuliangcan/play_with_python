# Problem: 小d和图片压缩
# Contest: NowCoder
# URL: https://ac.nowcoder.com/acm/contest/53366/B
# Memory Limit: 524288 MB
# Time Limit: 2000 ms

import sys

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')

MOD = 10 ** 9 + 7
PROBLEM = """
"""


#       ms
def solve():
    n, m = RI()
    g = []
    for _ in range(n):
        g.append(RILST())
    for i in range(0, n, 2):
        for j in range(0, m, 2):
            c = (g[i][j] + g[i + 1][j] + g[i + 1][j + 1] + g[i][j + 1]) // 4
            print(c, end=' ')
        print()


if __name__ == '__main__':
    solve()
