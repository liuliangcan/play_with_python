# Problem: 数字替换
# Contest: AcWing
# URL: https://www.acwing.com/problem/content/4871/
# Memory Limit: 256 MB
# Time Limit: 1000 ms

import sys
from collections import *

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')

MOD = 10 ** 9 + 7
PROBLEM = """
"""


#       ms
def solve():
    n, x = RI()
    ans = 0
    s = str(x)
    if len(s) == n:
        return print(0)
    if '0' in s and n == 1:
        return print(1)
    if n < len(s):
        return print(-1)
    if max(s) == '1':
        return print(-1)
    q = deque([x])
    vis = {x}
    while q:
        ans += 1
        for _ in range(len(q)):
            x = q.popleft()
            s = str(x)
            for i in s:
                y = x * int(i)
                if len(str(y)) == n:
                    return print(ans)
                if y not in vis:
                    vis.add(y)
                    q.append(y)
    print(-1)


if __name__ == '__main__':
    solve()
