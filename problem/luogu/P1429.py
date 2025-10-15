# Problem: P1429 平面最近点对（加强版）
# Contest: Luogu
# URL: https://www.luogu.com.cn/problem/P1429
# Memory Limit: 256 MB
# Time Limit: 1000 ms

import sys

from math import sqrt, inf

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())


def dis2(x1, y1, x2, y2):
    return (x1 - x2) ** 2 + (y1 - y2) ** 2


#       ms
def solve():
    s = sys.stdin.buffer.readline().strip()
    if not s:
        n, = RI()
    else:
        n = int(s)
    a = []
    for _ in range(n):
        x, y = RI()
        a.append((x, y))

    a.sort()
    b = sorted(range(n), key=lambda i: a[i][1])

    def dfs(l, r, ys):
        if r - l + 1 <= 3:
            ret = inf
            for i in range(l, r):
                for j in range(i + 1, r + 1):
                    ret = min(ret, dis2(a[i][0], a[i][1], a[j][0], a[j][1]))
            return ret
        mid = (l + r) >> 1
        x0 = a[mid][0]
        ys1, ys2 = [i for i in ys if a[i][0] <= x0], [i for i in ys if a[i][0] > x0]
        ret = min(dfs(l, mid, ys1), dfs(mid + 1, r, ys2))
        ys = [a[i] for i in ys if (a[i][0] - x0) ** 2 <= ret]
        for i, (x1, y1) in enumerate(ys):
            for j in range(i + 1, len(ys)):
                x2, y2 = ys[j]
                if (y2 - y1) ** 2 >= ret: break
                ret = min(ret, dis2(x1, y1, x2, y2))
        return ret

    ans = dfs(0, n - 1, b)
    print(f'{sqrt(ans):.4f}')


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
