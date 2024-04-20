import sys

sys.setrecursionlimit(10 ** 5 + 10)

"""
美团笔试题
输入n(1<=n<=1e5)表示树上n个节点。输入a[i](1<=a[i]<=2)表示每个节点的权值。
输入n-1条边。
问有多少条简单路径，权值乘积是完全平方数
输入
3
1 2 2
1 2 
2 3
输出
2
"""
"""由于节点权值只有1或2，那么其实就是看这条路径上2的数量是偶数。
考虑树形DP+乘法原理。
定义f[u][0/1]代表以u为根的子树时，子节点里到u的路径上2数量是偶数的节点数/奇数的节点数。
那么一共2种路径：1.子树到u(分类讨论)，2.子树到另一颗子树(乘法原理)
1. 子树到u：
    - 若a[u]=1,则子树里所有路径添加一个u，奇偶性保持不变，ans+=f[v][0]
    - 若a[u]=2,则子树里所有路径添加一个u，奇偶性翻转，ans+=f[v][1]
2. 子树到子树：
    用状态机dp理解：
    - 若a[u]=1,那么当前子树状态0结合前边所有子树状态0；状态1结合状态1
    - 若a[u]=2,那么状态1结合状态0；相反同理。
转移：
    讨论a[u]进行转移，最后别忘了更新本节点。
"""
def solve1():
    n = int(input())
    a = list(map(int, input().split()))
    g = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        g[u - 1].append(v - 1)
        g[v - 1].append(u - 1)
    ans = 0

    def dfs(u, fa):  # 返回子树里多少个点到u的路径2的奇偶数
        nonlocal ans
        cnts = []
        for v in g[u]:
            if v == fa: continue
            cnts.append(dfs(v, u))

        cnt = [0, 0]
        if cnts:
            if a[u] == 1:
                p = q = 0
                for x, y in cnts:
                    ans += x * p + y * q
                    p += x
                    q += y
                    cnt[0] += x
                    cnt[1] += y
            else:
                p = q = 0
                for x, y in cnts:
                    ans += x * q + y * p
                    p += x
                    q += y
                    cnt[0] += y
                    cnt[1] += x

        ans += cnt[0]
        if a[u] == 1:
            cnt[0] += 1
        else:
            cnt[1] += 1
        return cnt

    dfs(0, -1)
    print(ans)


def solve():
    n = int(input())
    a = list(map(int, input().split()))
    g = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        g[u - 1].append(v - 1)
        g[v - 1].append(u - 1)
    ans = 0

    order = []
    q = [0]
    fa = [-1] * n
    while q:
        u = q.pop()
        order.append(u)
        for v in g[u]:
            if v == fa[u]: continue
            fa[v] = u
            q.append(v)
    f = [[0, 0] for _ in range(n)]
    for u in order[::-1]:
        cnts = []
        for v in g[u]:
            if v == fa[u]: continue
            cnts.append(f[v])
        cnt = f[u]
        if cnts:
            if a[u] == 1:
                p = q = 0
                for x, y in cnts:
                    ans += x * p + y * q
                    p += x
                    q += y
                    cnt[0] += x
                    cnt[1] += y
            else:
                p = q = 0
                for x, y in cnts:
                    ans += x * q + y * p
                    p += x
                    q += y
                    cnt[0] += y
                    cnt[1] += x

        ans += cnt[0]
        if a[u] == 1:
            cnt[0] += 1
        else:
            cnt[1] += 1

    print(ans)



solve()
