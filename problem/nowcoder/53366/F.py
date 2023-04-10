# Problem: 小d和送外卖
# Contest: NowCoder
# URL: https://ac.nowcoder.com/acm/contest/53366/F
# Memory Limit: 524288 MB
# Time Limit: 2000 ms

import sys
from collections import deque
from math import inf
from types import GeneratorType

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')

MOD = 10 ** 9 + 7
PROBLEM = """
"""


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


#    1455   ms
def solve1():
    n, m = RI()
    g = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = RI()
        u -= 1
        v -= 1
        g[u].append(v)
        g[v].append(u)
    k, = RI()
    a = RILST()
    if k <= m:
        return print(0)
    s = set(x - 1 for x in a)
    # print(s)
    cnt = [0] * n  # 如果要送完这个子树的所有订单，要访问多少个节点；答案是边数*2，即(cnt[i]-1)*2
    yes = [0] * n  # 每个子树下共有几个订单

    p = []  # 子树的分组背包,p[i]代表如果这个子树里退i个单，最多能省几个需要访问的节点

    @bootstrap
    def dfs(u, fa):
        f = [0] + [-inf] * m  # 当前子树如果一个都不退，就不能省节点
        yes[u] = int(u in s)  # 如果本节点有订单，则订单数+1
        for v in g[u]:
            if v == fa: continue
            yield dfs(v, u)

            if yes[v]:  # 如果子树有订单，要累计过来，且路过的节点也要累计
                yes[u] += yes[v]
                cnt[u] += cnt[v]

            for j in range(m, 0, -1):
                for v, w in enumerate(p):
                    if v <= j:
                        f[j] = max(f[j], f[j - v] + w)
                    else:
                        break

        if yes[u]:  # 如果这个子树有订单，则这个加上这个节点
            cnt[u] += 1

        if yes[u] <= m:  # 如果这个子树下的所有订单不超过m，则可以尝试剪掉整个子树。
            f[yes[u]] = cnt[u]
        p[:] = f[:]
        yield

    dfs(0, -1)
    # print(cnt)
    # print(yes)

    print((cnt[0] - 1 - max(p)) * 2)


#     1447ms  ms
def solve2():
    n, m = RI()
    g = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = RI()
        u -= 1
        v -= 1
        g[u].append(v)
        g[v].append(u)
    k, = RI()
    a = RILST()
    if k <= m:
        return print(0)
    s = set(x - 1 for x in a)
    # print(s)
    cnt = [0] * n  # 如果要送完这个子树的所有订单，要访问多少个节点；答案是边数*2，即(cnt[i]-1)*2
    yes = [0] * n  # 每个子树下共有几个订单

    @bootstrap
    def dfs(u, fa):
        yes[u] = int(u in s)
        for v in g[u]:
            if v == fa: continue
            yield dfs(v, u)
            if yes[v]:
                yes[u] += yes[v]
                cnt[u] += cnt[v]
        if yes[u]:
            cnt[u] += 1

        yield

    dfs(0, -1)
    # print(cnt)
    # print(yes)
    p = []

    @bootstrap
    def dfs2(u, fa):
        f = [0] + [-inf] * m
        for v in g[u]:
            if v == fa: continue
            yield dfs2(v, u)
            for j in range(m, 0, -1):
                for v, w in enumerate(p):
                    if v <= j:
                        f[j] = max(f[j], f[j - v] + w)
                    else:
                        break
        if yes[u] <= m:
            f[yes[u]] = cnt[u]
            # print(u, f)
        p[:] = f[:]
        yield

    dfs2(0, -1)
    print((cnt[0] - 1 - max(p)) * 2)


#   1587ms  怎么bfs还慢了呢，可能是因为所有分组背包都要储存，空间用的多
def solve():
    n, m = RI()
    g = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = RI()
        u -= 1
        v -= 1
        g[u].append(v)
        g[v].append(u)
    k, = RI()
    a = RILST()
    if k <= m:
        return print(0)
    s = set(x - 1 for x in a)
    # print(s)
    cnt = [0] * n  # 如果要送完这个子树的所有订单，要访问多少个节点；答案是边数*2，即(cnt[i]-1)*2
    yes = [0] * n  # 每个子树下共有几个订单

    pp = [[] for _ in range(n)]
    fas = [-1] * n
    order = []
    q = deque([0])
    while q:
        u = q.popleft()
        order.append(u)
        for v in g[u]:
            if v == fas[u]: continue
            fas[v] = u
            q.append(v)

    for u in order[::-1]:
        yes[u] = int(u in s)
        f = [0] + [-inf] * m
        for v in g[u]:
            if v == fas[u]: continue
            if yes[v]:
                yes[u] += yes[v]
                cnt[u] += cnt[v]
            p = pp[v]
            for j in range(m, 0, -1):
                for v, w in enumerate(p):
                    if v <= j:
                        f[j] = max(f[j], f[j - v] + w)
                    else:
                        break
        if yes[u]:
            cnt[u] += 1
        if yes[u] <= m:
            f[yes[u]] = cnt[u]
        pp[u] = f

    print((cnt[0] - 1 - max(pp[0])) * 2)


if __name__ == '__main__':
    solve()
