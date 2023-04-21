# Problem: Chef and Battery
# Contest: CodeChef - START86D
# URL: https://www.codechef.com/START86D/problems/FIFTYPE
# Memory Limit: 256 MB
# Time Limit: 1000 ms

import sys
from collections import *

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')


#       ms
def solve():
    n, = RI()
    if n == 50:
        return print(0)
    t = 0
    vis = {n}
    q = deque([n])
    while q:
        t += 1
        for _ in range(len(q)):
            u = q.popleft()
            for v in u - 3, u + 2:
                if v == 50:
                    return print(t)
                if v < 0 or v > 100:
                    continue
                if v not in vis:
                    vis.add(v)
                    q.append(v)


if __name__ == '__main__':
    t, = RI()
    for _ in range(t):
        solve()
