"""换根DP，通过O(n)求出以0为根的树的性质，然后用低成本O(1)计算以1、2..n为根的性质
以max性质为例需要两次dfs:
1. dfs(0,-1):自下而上，求出tree[0]的性质，同时计算每个子树的性质down1[]+down2[]，分别代表当前节点的最大子树和次大子树的性质
2. reroot(0,-1):自上而下，通过父节点求子节点，子节点上升父节点下降来推算子树，计算up[i]，代表以i为节点向上的子树性质
    - 计算时：如果v在u的最大子树里，那么以v为根的up，则只能从down2[u]转移而来，或者从up[u]而来：up[v] = max(down2[u]+xx,up[u]+xx)
    -       如果v不在最大子树里，则可以从down1[u]转移而来。up[v] = max(down1[u]+xx,up[u]+xx)
3. 最终每个根的答案则是max(down1[i],up[i]) for i in range(n)
---
sum性质与max相比有所不通，通常不需要down1,down2,up三个复杂数组，大部分只需要一个数组。
1. dfs自下而上不变
2. reroot时，u->v转移通常并不需要考虑最大次大等性质，可直接转移：想象抓着着根节点的相邻儿子向上提↑，那么根的性质减去、儿子的性质加上即可。
---
cf等oj上，py的dfs容易爆，可能需要装饰器强行递归；或者通过bfs事先计算遍历顺序，保证每个父节点在子树前边访问即可。这样只需要正序一遍、倒序一遍

例题：
https://blog.csdn.net/liuliangcan/article/details/128749634
max模型：
    - 310. 最小高度树 https://leetcode.cn/problems/minimum-height-trees/?envType=daily-question&envId=2024-03-17
    - 树的直径 https://www.acwing.com/problem/content/description/4802/
sum模型：
    - 2581. 统计可能的树根数目 https://leetcode.cn/problems/count-number-of-possible-root-nodes/description/
    - E. Tree Painting https://codeforces.com/problemset/problem/1187/E
"""

### max版
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        down1 = [0] * n
        down2 = [0] * n
        up = [0] * n

        def dfs(u, fa):

            for v in g[u]:
                if v == fa:
                    continue
                h = dfs(v, u)
                h += 1
                if h > down1[u]:
                    down2[u] = down1[u]
                    down1[u] = h
                elif h > down2[u]:
                    down2[u] = h
            return down1[u]

        dfs(0, -1)

        def reroot(u, fa):
            for v in g[u]:
                if v == fa: continue
                if down1[u] == down1[v] + 1:
                    up[v] = max(down2[u] + 1, up[u] + 1)
                else:
                    up[v] = max(down1[u] + 1, up[u] + 1)
                reroot(v, u)

        reroot(0, -1)
        f = [max(x, y) for x, y in zip(up, down1)]
        mn = min(f)
        return [i for i, v in enumerate(f) if v == mn]


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        fa = [-1] * n
        order = []
        q = [0]
        while q:
            u = q.pop()
            order.append(u)
            for v in g[u]:
                if v == fa[u]:
                    continue
                fa[v] = u
                q.append(v)

        down1 = [0] * n
        down2 = [0] * n
        up = [0] * n

        for u in order[::-1]:
            for v in g[u]:
                if v == fa[u]: continue
                h = down1[v] + 1
                if h > down1[u]:
                    down2[u] = down1[u]
                    down1[u] = h
                elif h > down2[u]:
                    down2[u] = h
        for u in order:
            for v in g[u]:
                if v == fa[u]: continue
                if down1[u] == down1[v] + 1:
                    up[v] = max(down2[u] + 1, up[u] + 1)
                else:
                    up[v] = max(down1[u] + 1, up[u] + 1)

        f = [max(x, y) for x, y in zip(up, down1)]
        mn = min(f)
        return [i for i, v in enumerate(f) if v == mn]


### sum版
#    1111   ms
def solve1():
    n, = RI()
    g = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = RI()
        g[u - 1].append(v - 1)
        g[v - 1].append(u - 1)

    cnt = [1] * n
    down = [0] * n

    @bootstrap
    def dfs(u, fa):
        for v in g[u]:
            if v == fa: continue
            yield dfs(v, u)
            cnt[u] += cnt[v]
            down[u] += down[v]
        down[u] += cnt[u]
        yield

    dfs(0, -1)

    @bootstrap
    def reroot(u, fa):
        for v in g[u]:
            if v == fa: continue
            down[v] = down[u] - cnt[v] + n - cnt[v]
            yield reroot(v, u)
        yield

    reroot(0, -1)
    print(max(down))


#  514     ms
def solve():
    n, = RI()
    g = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = RI()
        g[u - 1].append(v - 1)
        g[v - 1].append(u - 1)

    fa = [-1] * n
    order = []
    q = [0]
    while q:
        u = q.pop()
        order.append(u)
        for v in g[u]:
            if v == fa[u]:
                continue
            fa[v] = u
            q.append(v)

    cnt = [1] * n
    down = [0] * n

    for u in order[::-1]:
        for v in g[u]:
            if v == fa[u]: continue
            cnt[u] += cnt[v]
            down[u] += down[v]
        down[u] += cnt[u]

    for u in order:
        for v in g[u]:
            if v == fa[u]: continue
            down[v] = down[u] - cnt[v] + n - cnt[v]

    print(max(down))
