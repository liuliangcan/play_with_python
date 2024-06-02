"""无向图n^2找环详细，顺便缩点 ，如果保证没有一个点在多个环上，那复杂度好像是o(n)

"""


def find_circles(g,n,start=0):
    """
    g 是无向图
    n 是最大点，0-indexed,如果你是1~n,那么传n+1进来
    start是起点，暂时没想到有啥需要改的
    返回
        circles:是一个{fa:[1,3,5]},这个环的代表元和内容
        dsu: 环合并后的并查集
    """
    dsu = DSU(n)
    path = []
    pp = set()
    vis = [0] * n
    circles = {}

    def dfs(u, fa):
        path.append(u)
        pp.add(u)
        for v in g[u]:
            if v == fa: continue
            if vis[v] and v in pp:
                if dsu.find_fa(v) in circles: continue
                # print(path,u,v)
                p = []
                i = len(path) - 1
                while i >= 0:
                    p.append(path[i])
                    if path[i] == v:
                        break
                    i -= 1
                if len(p) > 2:
                    for v in p[1:]:
                        dsu.union(p[0], v)
                circles[dsu.find_fa(p[0])] = p
            else:
                vis[v] = 1
                dfs(v, u)
        path.pop()
        pp.remove(u)
    dfs(start,-1)
    return circles,dsu