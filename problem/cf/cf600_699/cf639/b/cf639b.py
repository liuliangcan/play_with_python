import os
import sys

import sortedcontainers as sortedcontainers

if os.getenv('LOCALCFTEST'):
    sys.stdin = open('../../../../../before20221227/cf/cfinput.txt')
MOD = 10 ** 9 + 7

"""https://codeforces.com/problemset/problem/639/B

【易错题】
输入三个正整数 n(2<=n<=1e5), d 和 h(1<=h<=d<=n-1)。

请你构造一棵有 n 个节点，直径为 d，高度为 h 的无向树。
若无法构造，输出 -1；否则输出这棵树，用 n-1 条边表示（任意一种合法构造方案均可，节点的编号从 1 开始）。

直径：树上任意两节点的最远距离。
高度：节点 1 和任意节点的最远距离。"""
"""https://codeforces.com/problemset/submission/639/163977647

先说一般的构造逻辑：
1. 构造一条从 1 出发，长为 h 的链。
2. 如果 h<d，则构造另一条从 1 出发，长为 d-h 的链，这样直径就构造好了。
3. 其余点连到 2 上。

为了满足这个构造的条件，需要特判的东西还是挺多的：
1. 用两条长为 h 的链可以拼成长为 2h 的直径。如果 d>2h，返回 -1。
2. 特判 d=1，那么 n 只能是 2，否则返回 -1。
3. 特判 n=2，输出 1-2。
4. 特判 h=1，这个时候所有点只能连到 1 上，输出 1-2, 1-3, ..., 1-n。
5. 然后就是一般的构造了。"""
def solve(n, d, h):
    if 2 * h < d or (d == 1 and n > 2):
        print(-1)
        return
    if n == 2:
        print(1, 2)
        return
    if h == 1:
        for i in range(2, n + 1):
            print(1, i)
        return

    for i in range(1, h + 1):  # 从1，一条高h的链
        print(i, i + 1)

    if d > h:  # 从1，一条d-h的链
        print(1, h + 2)
        for i in range(h + 2, d + 1):
            print(i, i + 1)
    # 剩下的全挂2上
    for i in range(d + 2, n + 1):
        print(2, i)


if __name__ == '__main__':
    n, d, h = map(int, input().split())
    # print(n,d,h)
    solve(n, d, h)
    a = sortedcontainers.SortedList()
