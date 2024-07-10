import sys

from heapq import heappop, heappush

RI = lambda: map(int, sys.stdin.buffer.readline().split())
print = lambda d: sys.stdout.write(
    str(d) + "\n")  # 打开可以快写，但是无法使用print(*ans,sep=' ')这种语法,需要print(' '.join(map(str, p)))，确实会快。

inf = 10 ** 16
"""py时限1s，太卡了。
但是学到了一招，可以把正反图放到一个长度*2的图里模拟。
这种跑完正图直接跑反图，把自己和自己在反图上连起来即可。
"""
n, m = RI()
g = [[(u + n, 0)] if u <= n else [] for u in range(n << 1 | 1)]
for _ in range(m):
    u, v, w = RI()
    g[u].append((v, w))
    g[v + n].append((u + n, w))

dis = [inf] * (n << 1 | 1)
dis[1] = 0

mask = (1 << 20) - 1

q = [1]
while q:
    s = heappop(q)
    c, u = s >> 20, s & mask
    if c > dis[u]: continue
    for v, w in g[u]:
        d = w + c
        if d < dis[v]:
            dis[v] = d
            heappush(q, d << 20 | v)

print(' '.join(map(lambda x: str(x) if x < inf else '-1', dis[n + 2:])))
# def dij(q, g):
#     while q:
#         s = heappop(q)
#         c, u = s >> 20, s & mask
#         if c > dis[u]: continue
#         for v, w in g[u]:
#             d = w + c
#             if d < dis[v]:
#                 dis[v] = d
#                 heappush(q, d << 20 | v)
#
#
# dij([1], g)
# dij([d << 20 | u for u, d in enumerate(dis) if d < inf], rg)
# print(' '.join(map(lambda x: str(x) if x < inf else '-1', dis[2:])))
# print(' '.join([str(dis[i]) if dis[i] < inf else '-1' for i in range(2, n + 1)]))
# def dij(q, g):
#     while q:
#         c, u = heappop(q)
#         if c > dis[u]: continue
#         for v, w in g[u]:
#             d = w + c
#             if d < dis[v]:
#                 dis[v] = d
#                 heappush(q, (d, v))
#
#
# dij([(0, 1)], g)
# dij([(d, u) for u, d in enumerate(dis) if d < inf], rg)
# print(' '.join(map(lambda x: str(x) if x < inf else '-1', dis[2:])))
