# Problem: 最短路之和/*-/*-/*-/*-
# Contest: AcWing
# URL: https://www.acwing.com/problem/content/4875/
# Memory Limit: 256 MB
# Time Limit: 3000 ms

import sys

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')

MOD = 10 ** 9 + 7
PROBLEM = """
"""


#     6995  ms
def solve():
    n, = RI()
    d = []
    for _ in range(n):
        d.append(RILST())
    xs = RILST()
    ans = []
    ps = []
    for x in xs[::-1]:
        k = x - 1
        # 注意 上两个循环可以合并(顺序随意)，但这个循环必须在最后，否则会wa
        # 前提是所有其它点到k的最短路(即所有uk/kv)求出来，才可以用k来松弛uv的边。
        for u in range(n):
            for v in range(n):
                d[u][v] = min(d[u][v], d[u][k] + d[k][v])

        ps.append(k)
        a = 0
        for u in ps:
            for v in ps:
                a += d[u][v]
        ans.append(a)
    print(*(ans[::-1]))


#     10039   ms
def solve1():
    n, = RI()
    d = []
    for _ in range(n):
        d.append(RILST())
    xs = RILST()
    ans = []
    ps = []
    for x in xs[::-1]:
        k = x - 1
        a = 0

        # 尝试用所有v松弛uk，这里uv已经是最短路，所以可以松弛
        for u in ps:
            for v in ps:
                d[u][k] = min(d[u][k], d[u][v] + d[v][k])
            a += d[u][k]
        # 尝试用所有v松弛ku，这里uv已经是最短路，所以可以松弛
        for u in ps:
            for v in ps:
                d[k][u] = min(d[k][u], d[k][v] + d[v][u])
            a += d[k][u]

        # 注意 上两个循环可以合并(顺序随意)，但这个循环必须在最后，否则会wa
        # 前提是所有其它点到k的最短路(即所有uk/kv)求出来，才可以用k来松弛uv的边。
        for u in ps:
            for v in ps:
                d[u][v] = min(d[u][v], d[u][k] + d[k][v])
                a += d[u][v]

        ps.append(k)
        ans.append(a)
    print(*(ans[::-1]))


if __name__ == '__main__':
    solve()
