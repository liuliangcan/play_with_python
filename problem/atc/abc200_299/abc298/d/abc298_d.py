# Problem: D - Writing a Numeral
# Contest: AtCoder - TOYOTA MOTOR CORPORATION Programming Contest 2023#1 (AtCoder Beginner Contest 298)
# URL: https://atcoder.jp/contests/abc298/tasks/abc298_d
# Memory Limit: 1024 MB
# Time Limit: 3000 ms

import sys
from collections import *

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')
print = lambda d: sys.stdout.write(
    str(d) + "\n")  # 打开可以快写，但是无法使用print(*ans,sep=' ')这种语法,需要print(' '.join(map(str, p)))，确实会快。

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 右下左上
DIRS8 = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0),
         (-1, 1)]  # →↘↓↙←↖↑↗
# MOD = 10**9 + 7
MOD = 998244353
PROBLEM = """https://atcoder.jp/contests/abc298/tasks/abc298_d

最初 S="1"。
输入 q(≤6e5) 和 q 个操作，操作的输入格式如下：
如果输入的是 1 x，把 x 加到 S 末尾。其中 1≤x≤9。
如果输入的是 2，删除 S 的第一个数字。
如果输入的是 3，把 S 视作一个整数，输出它模 998244353 的结果。
"""
"""取模小练习。

设当前数字为 cur，用队列维护 s。
操作 1 是 cur = cur * 10 + x，把 x 加到 s 末尾。
操作 2 是 cur = cur - s[0] * pow(10, len(s)-1)，弹出 s 队首。
注意取模。由于减法会产生负数，在输出答案的时候要调整为非负数。

代码实现时，预处理 pow(10, ...) 或者用逆元，可以做到线性时间。

https://atcoder.jp/contests/abc298/submissions/44656651"""


#      304  ms
def solve():
    q, = RI()
    s = 1
    dq = deque([1])
    pw = 1
    inv10 = pow(10, MOD - 2, MOD)
    for _ in range(q):
        t, *x = RI()
        if t == 1:
            dq.append(x[0])
            s = (s * 10 + x[0]) % MOD
            pw = pw * 10 % MOD
        elif t == 2:
            s = (s - dq.popleft() * pw) % MOD
            pw = pw * inv10 % MOD
        else:
            print(s)


#      324  ms
def solve1():
    q, = RI()
    s = 1
    dq = deque([1])
    pw = [1]
    for _ in range(q):
        pw.append(pw[-1] * 10 % MOD)

    for _ in range(q):
        t, *x = RI()
        if t == 1:
            dq.append(x[0])
            s = (s * 10 + x[0]) % MOD
        elif t == 2:
            s = (s - dq.popleft() * pw[len(dq)]) % MOD
        else:
            print(s)


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
