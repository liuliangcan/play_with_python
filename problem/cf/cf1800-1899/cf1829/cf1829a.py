# Problem: A. Love Story
# Contest: Codeforces - Codeforces Round 871 (Div. 4)
# URL: https://codeforces.com/contest/1829/problem/A
# Memory Limit: 256 MB
# Time Limit: 1000 ms

import sys

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')
# print = lambda d: sys.stdout.write(str(d) + "\n")  # 打开可以快写，但是无法使用print(*ans,sep=' ')这种语法

MOD = 10 ** 9 + 7
PROBLEM = """https://codeforces.com/contest/1829/problem/A
输入t组数据。
每组数据输入一个长为10的字符串。
计算有几个位置不对应"codeforces"
"""


#       ms
def solve():
    s, = RS()
    p = 'codeforces'
    ans = 0
    for a, b in zip(p, s):
        if a != b:
            ans += 1
    print(ans)


if __name__ == '__main__':
    t, = RI()
    for _ in range(t):
        solve()
