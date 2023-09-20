# Problem: 小美的子序列
# Contest: NowCoder
# URL: https://ac.nowcoder.com/acm/contest/65051/B
# Memory Limit: 524288 MB
# Time Limit: 2000 ms

import sys

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')
# print = lambda d: sys.stdout.write(str(d) + "\n")  # 打开可以快写，但是无法使用print(*ans,sep=' ')这种语法,需要print(' '.join(map(str, p)))，确实会快。

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 右下左上
DIRS8 = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0),
         (-1, 1)]  # →↘↓↙←↖↑↗
MOD = 10 ** 9 + 7
# MOD = 998244353
PROBLEM = """其实是子序列问题，用双指针往后移动即可
"""


#       ms
def solve():
    n, m = RI()
    i = 0
    s = 'meituan'
    for _ in range(n):
        row, = RS()
        if i == len(s): continue
        if s[i] in row:
            i += 1

    if i == len(s):
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
