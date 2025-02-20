import sys

from collections import deque

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())

PROBLEM = """https://codeforces.com/contest/1064/problem/d
带墙网格图，分别限制左右可以走l,r步，上下走不限制，问可达点有多少个

先说结论：直接BFS即可，状态变化只有0（不走或者竖着走）和1（横着走），先左先右没有区别。
考虑从a点到b点，他俩不同行，这中间花费的向左向右步数分别为l,r，可以发现l-r的值是固定的，因为如果中途向左多走一步，那么向右也要多一步。
所以我们只需要最小化l或者r或者总步数(l+r)即可。
直接BFS就等于最小化总步数,由于这里有竖着走的操作，所以要用01BFS
"""


def solve():  # 搞抽象
    n, m = RI()
    sx, sy = RI()
    sl, sr = RI()
    g = []
    for _ in range(n):
        s, = RS()
        g.append([-1 if c == '.' else -2 for c in s])
    sx -= 1
    sy -= 1
    q = deque([sx << 11 | sy])
    mask = (1 << 11) - 1
    g[sx][sy] = sr  # 存还有多少次右可以走
    ans = 0
    while q:
        ans += 1
        xy = q.popleft()
        x, y = xy >> 11, xy & mask
        r = g[x][y]
        l = sl + y - sy - sr + r  # y-sy = sr-r - (sl-l)
        for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
            a, b = x + dx, y + dy
            if 0 <= a < n and 0 <= b < m and g[a][b] == -1:
                if b == y:  # 竖着走
                    g[a][b] = r
                    q.appendleft(a << 11 | b)
                else:
                    if b < y:
                        if l:
                            g[a][b] = r
                            q.append(a << 11 | b)
                    elif b > y and r:
                        g[a][b] = r - 1
                        q.append(a << 11 | b)
    print(ans)


def solve2():  # 781
    n, m = RI()
    sx, sy = RI()
    sl, sr = RI()
    g = []
    for _ in range(n):
        s, = RS()
        g.append([-1 if c == '.' else -2 for c in s])
    sx -= 1
    sy -= 1
    q = deque([(sx, sy)])
    g[sx][sy] = sr  # 存还有多少次右可以走
    ans = 0
    while q:
        ans += 1
        x, y = q.popleft()
        r = g[x][y]
        l = sl + y - sy - sr + r  # y-sy = sr-r - (sl-l)
        for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
            a, b = x + dx, y + dy
            if 0 <= a < n and 0 <= b < m and g[a][b] == -1:
                if b == y:  # 竖着走
                    g[a][b] = r
                    q.appendleft((a, b))
                else:
                    if b < y:
                        if l:
                            g[a][b] = r
                            q.append((a, b))
                    elif b > y and r:
                        g[a][b] = r - 1
                        q.append((a, b))
    print(ans)


def solve1():
    n, m = RI()
    x, y = RI()
    l, r = RI()
    g = []
    for _ in range(n):
        s, = RS()
        g.append([-1 if c == '.' else -2 for c in s])
    q = deque([(x - 1, y - 1, l)])
    g[x - 1][y - 1] = r
    ans = 0
    while q:
        ans += 1
        x, y, l = q.popleft()
        r = g[x][y]
        for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
            a, b = x + dx, y + dy
            if 0 <= a < n and 0 <= b < m and g[a][b] == -1:
                if b == y:  # 竖着走
                    g[a][b] = r
                    q.appendleft((a, b, l))
                else:
                    if b < y:
                        if l:
                            g[a][b] = r
                            q.append((a, b, l - 1))
                    elif b > y and r:
                        g[a][b] = r - 1
                        q.append((a, b, l))
    print(ans)


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
