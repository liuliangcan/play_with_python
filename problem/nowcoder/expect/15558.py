# Problem: 取手机
# Contest: NowCoder
# URL: https://ac.nowcoder.com/acm/problem/15558
# Memory Limit: 2 MB
# Time Limit: 15558000 ms

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
"""从b中选一个放在第k个位置
p=b*剩下a+b-1各位置全排列，
s=a+b个位置全排列
ans = b*perm(a+b-1)/perm(a+b)=b/(a+b)
"""

#       ms
def solve():
    a, b, k = RI()
    if a == 0:
        return 1
    if b == 0:
        return 0
    return b/(a+b)



if __name__ == '__main__':
    t = 1
    if t:
        t, = RI()
        for _ in range(t):
            print(f'{solve():.3f}')
    else:
        solve()
