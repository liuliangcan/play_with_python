# Problem: G. Orray
# Contest: Codeforces - Codeforces Round 827 (Div. 4)
# URL: https://codeforces.com/contest/1742/problem/G
# Memory Limit: 256 MB
# Time Limit: 2000 ms

import sys

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')
print = lambda d: sys.stdout.write(
    str(d) + "\n")  # 打开可以快写，但是无法使用print(*ans,sep=' ')这种语法,需要print(' '.join(map(str, p)))，确实会快。

MOD = 10 ** 9 + 7
PROBLEM = """最多取30次max
"""


#    155   ms
def solve():
    n, = RI()
    a = RILST()
    p = []
    s = 0
    c = min(29, n - 1)
    for k in range(c, -1, -1):
        mx = 0
        for i, v in enumerate(a):
            if v | s > a[mx] | s:
                mx = i
        # print(mx,a)
        s |= a[mx]
        p.append(a[mx])
        a.pop(mx)
    print(' '.join(map(str, p)) + ' ' + ' '.join(map(str, a)))


if __name__ == '__main__':
    t = 1
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
