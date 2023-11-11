# Problem: D. Minesweeper 1D
# Contest: Codeforces - Codeforces Round 237 (Div. 2)
# URL: https://codeforces.com/contest/404/problem/D
# Memory Limit: 512 MB
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
PROBLEM = """https://codeforces.com/contest/404/problem/D

输入一个长度在 [1,1e6] 内的字符串，由五种字符 *?012 组成，表示一个「一维扫雷游戏」的局面。
其中 * 表示雷，数字表示左右相邻位置有多少个雷。
把 ? 替换成 *012 中的一个，可以得到多少个合法的局面？模 1e9+7。

输入 ?01???
输出 4
解释 有 001**1, 001***, 001*2*, 001*10 这四种合法局面

输入 ?
输出 2

输入 **12
输出 0

输入 1
输出 0
"""


#       ms
def solve():
    s, = RS()
    x, y, z = 1, 0, 1  # 不是雷/是雷/右边是雷
    for c in s:
        if c == '0':
            x, y, z = x, 0, 0
        elif c == '1':
            x, y, z = y, 0, x
        elif c == '2':
            x, y, z = 0, 0, y
        elif c == '*':
            x, y, z = 0, z, z
        else:
            x, y, z = (x + y) % MOD, z, (x + y + z) % MOD
    print((x + y) % MOD)



if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
