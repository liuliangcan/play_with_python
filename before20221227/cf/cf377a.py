import sys
from collections import *
from itertools import *
from math import *
from array import *
from functools import lru_cache
import heapq
import bisect
import random
import io, os
from types import GeneratorType

if sys.hexversion == 50924784:
    sys.stdin = open('cfinput.txt')

# input = sys.stdin.readline
# input_int = sys.stdin.buffer.readline
RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: sys.stdin.readline().strip().split()
RILST = lambda: list(RI())


MOD = 10 ** 9 + 7
"""https://codeforces.com/problemset/problem/377/A

输入 n(≤500) m(≤500) k 和一个 n 行 m 列的网格图，'#' 表示墙，'.' 表示平地。
保证所有 '.' 可以互相到达（四方向连通）。保证 k 小于 '.' 的个数。
你需要把恰好 k 个 '.' 修改成 '#'，使得剩余的所有 '.' 仍然是可以互相到达的。
输出修改后的网格图。

输入
3 4 2
#..#
..#.
#...
输出
#.X#
X.#.
#...

输入
5 4 5
#...
#.#.
.#..
...#
.#.#
输出
#XXX
#X#.
X#..
...#
.#.#
"""


# bfs 312	 ms
def solve1(m, n, k, g):
    def print_g():
        for b in g:
            print(''.join(b))

    if k == 0:
        return print_g()

    points = []
    for i in range(m):
        for j in range(n):
            if g[i][j] == '.':
                points.append((i, j))

    k = len(points) - k  # 只能保留k个点

    def get_route():
        DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def inside(x, y):
            return 0 <= x < m and 0 <= y < n

        q = deque([points[0]])
        vis = set(q)
        if len(vis) == k:
            return vis
        while q:
            x, y = q.popleft()
            for dx, dy in DIRS:
                a, b = x + dx, y + dy
                if inside(a, b) and g[a][b] == '.' and (a, b) not in vis:
                    vis.add((a, b))
                    if len(vis) == k:
                        return vis
                    q.append((a, b))
        return vis

    # 除了路径上的点都改成X
    keep = get_route()
    for x, y in points:
        if (x, y) not in keep:
            g[x][y] = 'X'

    print_g()


# bfs翻过来做 直接从x修改到.;本题dfs 会爆栈 171 ms
def solve(m, n, k, g):
    def print_g():
        for b in g:
            print(''.join(b))

    if k == 0:
        return print_g()

    cnt = 0
    start = (0, 0)
    for i in range(m):
        for j in range(n):
            if g[i][j] == '.':
                g[i][j] = 'X'
                if 0 == cnt:
                    start = (i, j)
                cnt += 1

    k = cnt - k  # 只能保留k个点
    DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def inside(x, y):
        return 0 <= x < m and 0 <= y < n

    g[start[0]][start[1]] = '.'
    k -= 1
    if k == 0:
        return print_g()
    q = deque([start])

    while q:
        x, y = q.popleft()
        for dx, dy in DIRS:
            a, b = x + dx, y + dy
            if inside(a, b) and g[a][b] == 'X':
                g[a][b] = '.'
                k -= 1
                if 0 == k:
                    return print_g()
                q.append((a, b))
    print_g()


# 155ms
def cf377a():
    n, m, k = RI()
    if k == 0:
        for _ in range(n):
            b, = RS()
            print(b)
    else:
        g = []
        cnt = 0
        for _ in range(n):
            b, = RS()
            cnt += b.count('.')
            g.append(list(b.replace('.', 'X')))
        m, n = n, m

        def get_start():
            for i in range(m):
                for j in range(n):
                    if g[i][j] == 'X':
                        return i, j

        start = get_start()

        def print_g():
            print('\n'.join(''.join(b) for b in g))

        k = cnt - k  # 只能保留k个点

        g[start[0]][start[1]] = '.'
        k -= 1
        if k == 0:
            return print_g()
        q = deque([start])

        while q:
            x, y = q.popleft()
            for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
                a, b = x + dx, y + dy
                if 0 <= a < m and 0 <= b < n and g[a][b] == 'X':
                    g[a][b] = '.'
                    k -= 1
                    if 0 == k:
                        return print_g()
                    q.append((a, b))
        print_g()


def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to

    return wrappedfunc


# dfs
def solve3(m, n, k, g):
    def print_g():
        print('\n'.join(''.join(b) for b in g))

    if k == 0:
        return print_g()
    cnt = sum(b.count('.') for b in g)
    k = cnt - k  # 只能保留k个点
    DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def inside(x, y):
        return 0 <= x < m and 0 <= y < n

    vis = set()

    @bootstrap
    def dfs2(x, y):
        vis.add((x, y))
        if len(vis) == k:
            yield None

        for dx, dy in DIRS:
            a, b = x + dx, y + dy
            if inside(a, b) and g[a][b] == '.' and (a, b) not in vis and len(vis) < k:
                yield dfs(a, b)
        yield None
    cnt = 0
    @bootstrap
    def dfs(x, y):
        nonlocal cnt
        cnt += 1
        print(cnt)
        if len(vis) == k:
            yield None
        vis.add((x, y))

        for dx, dy in DIRS:
            a, b = x + dx, y + dy
            if inside(a, b) and g[a][b] == '.' and (a, b) not in vis:
                yield dfs(a, b)
                # print(r)
                # if r is None:
                #     yield None
                # yield r

        yield None

    def dfs1(x, y):
        vis.add((x, y))
        if len(vis) == k:
            return True
        for dx, dy in DIRS:
            a, b = x + dx, y + dy
            if inside(a, b) and g[a][b] == '.' and (a, b) not in vis:
                if dfs(a, b):
                    return True
        return False

    for i in range(m):
        for j in range(n):
            if g[i][j] == '.':
                dfs(i, j)

                # print(vis)
                for x in range(m):
                    for y in range(n):
                        if g[x][y] == '.' and (x, y) not in vis:
                            g[x][y] = 'X'
                return print_g()


if __name__ == '__main__':
    n, m, k = RI()

    a = []
    for _ in range(n):
        b, = RS()
        a.append(list(b))

    solve(n, m, k, a)
    # cf377a()
