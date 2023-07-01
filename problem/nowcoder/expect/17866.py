# Problem: 谁是神射手
# Contest: NowCoder
# URL: https://ac.nowcoder.com/acm/problem/17866
# Memory Limit: 2 MB
# Time Limit: 17866000 ms

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
PROBLEM = """
"""
"""
a赢的概率是：先手和后手均失败i次，然后先手成功，即a*sum((1-a)**i * (1-b)**i)，其中i无限大逼近
b赢的概率是：先手多失败一次，然后后手先手均失败i次，后手陈工，即b*(1-a)(sum((1-a)**i * (1-b)**i)。
那么让a赢即 a*sum((1-a)**i * (1-b)**i) > b*(1-a)(sum((1-a)**i * (1-b)**i) 
    即 a > b*(1-a)
"""


#       ms
def solve():
    a, b = RI()
    if a * 100 > b * (100 - a):
        print('MWH')
    elif a * 100 < b * (100 - a):
        print('CSL')
    else:
        print('equal')


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
