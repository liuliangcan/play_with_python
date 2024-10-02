"""https://orac2.info/problem/fario19frogs/"""

import os.path
import sys
from math import inf

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
INFILE = ''
OUTFILE = ''
if INFILE and os.path.exists(INFILE):
    sys.stdin = open(INFILE, 'r')
if INFILE and os.path.exists(INFILE):
    sys.stdout = open(OUTFILE, 'w')
"""https://zhuanlan.zhihu.com/p/714599644
单调栈+dfn+RMQ
青蛙上学从i只能跳到最近的严格大于a[i]的位置，如果两边都有则选右边。
放学只能从j跳到最近的严格小于a[j]的位置，同样先选右边。
家到学校和学校到家步数都不能超过k。
问哪些个位置可以建家。

显然每个位置能跳的目标是固定的，因此可以逆序建两棵树（加个虚拟节点）。
dfs上学树，当前是u，那么route[-k-2:-1]，这k个都可以建学校（满足上学条件）
这k个里是否存在一个v,在放学树里从u向下k步内能找到v呢，满足的话就符合放学条件。
这句话在放学树可以变成两个事：
1. v在u的子树里。
2. dep[v]-dep[u]<=k

这提示我们直接查询u的子树里所有合法节点的min(dep)判断mn-dep[u]<=k。 这可以用dfn+RMQ解决
合法节点怎么判？dfs上学树时，维护最后的k个，出窗的时候设inf，否则设dep

"""

class ZKW:
    """自低向上非递归写法线段树，0_indexed
    tmx = ZKW(pre, max, -2 ** 61)
    """
    __slots__ = ('n', 'op', 'e', 'log', 'size', 'd')

    def __init__(self, V, OP, E):
        """
        V: 原数组
        OP: 操作:max,min,sum
        E: 每个元素默认值
        """
        self.n = len(V)
        self.op = OP
        self.e = E
        self.log = (self.n - 1).bit_length()
        self.size = 1 << self.log
        self.d = [E for i in range(2 * self.size)]
        for i in range(self.n):
            self.d[self.size + i] = V[i]
        for i in range(self.size - 1, 0, -1):
            self.update(i)

    def set(self, p, x):
        # assert 0 <= p and p < self.n
        update = self.update
        p += self.size
        self.d[p] = x
        for i in range(1, self.log + 1):
            update(p >> i)

    def get(self, p):
        # assert 0 <= p and p < self.n
        return self.d[p + self.size]

    def query(self, l, r):  # [l,r)左闭右开
        # assert 0 <= l and l <= r and r <= self.n
        sml, smr, op, d = self.e, self.e, self.op, self.d

        l += self.size
        r += self.size

        while l < r:
            if l & 1:
                sml = op(sml, d[l])
                l += 1
            if r & 1:
                smr = op(d[r - 1], smr)
                r -= 1
            l >>= 1
            r >>= 1
        return self.op(sml, smr)

    def all_query(self):
        return self.d[1]

    def update(self, k):
        self.d[k] = self.op(self.d[k << 1], self.d[k << 1 | 1])

    def __str__(self):
        return str([self.get(i) for i in range(self.n)])


class HLD:
    def __init__(self, g, root):
        # 无论是点还是dfn\rank还是dep，都从1开始，默认0是无
        n = len(g) - 1
        self.g = g
        self.fa = fa = [0] * (n + 1)  # 父节点，0表示无父节点
        self.size = size = [1] * (n + 1)  # 子树大小
        self.dep = dep = [0] * (n + 1)  # 深度，根深度为1
        self.son = son = [0] * (n + 1)  # 重儿子，0表示无儿子
        self.dfn = dfn = [0] * (n + 1)  # dfs序，子树终点的dfs序是dfn[i]+size[i]-1
        self.top = top = list(range(n + 1))  # 所在重链起点，起点就是自己
        self.rank = rank = [0] * (n + 1)  # dfs序为i的节点编号
        size[0] = 0
        st = [root]
        dep[root] = 1
        tot = 1
        while st:  # 第一次dfs：求fa\depth\size\hson
            u = st.pop()
            rank[tot] = u  # 临时算一个非重儿子优先的dfn序，用于自底向上计算size
            tot += 1
            for v in g[u]:
                if v == fa[u]: continue
                fa[v] = u  # 父节点
                dep[v] = dep[u] + 1  # 深度
                st.append(v)
        for u in rank[:0:-1]:  # 自底向上
            for v in g[u]:
                if v == fa[u]: continue
                size[u] += size[v]
                if size[v] > size[son[u]]: son[u] = v  # 更新重儿子

        for u in rank[1:]:  # 自上而下更新链起点  第二次dfs：求top\优先访问重儿子的dfn\rank
            for v in g[u]:
                if v == son[u]: top[v] = top[u]
        st = [root]
        tot = 1
        while st:  # 重新计算以重儿子优先的dfn序（可能有用）
            u = st.pop()
            dfn[u] = tot
            rank[tot] = u
            tot += 1
            if son[u] == 0: continue  # 叶子
            for v in g[u]:
                if v != fa[u] and v != son[u]: st.append(v)
            st.append(son[u])

def solve():
    n, k = RI()
    a = RILST()
    sys.setrecursionlimit(n+10)
    left,right = [-1]*n,[n]*n
    st = []
    for i, v in enumerate(a):
        while st and a[st[-1]] <= v:
            st.pop()
        if st:
            left[i] = st[-1]
        st.append(i)
    st = []
    for i, v in enumerate(a):
        while st and a[st[-1]] < v:
            right[st.pop()] = i
        st.append(i)
    g1 = [[] for _ in range(n+2)]
    for i, (l,r) in enumerate(zip(left,right)):
        cur = n
        d = n
        if r < n:
            d = r - i
            cur = r
        if l >= 0 and i-l < d:
            cur = l
        g1[cur+1].append(i+1)
    # print(g1)

    left, right = [-1] * n, [n] * n
    st = []
    for i, v in enumerate(a):
        while st and a[st[-1]] >= v:
            st.pop()
        if st:
            left[i] = st[-1]
        st.append(i)
    st = []
    for i, v in enumerate(a):
        while st and a[st[-1]] > v:
            right[st.pop()] = i
        st.append(i)
    g2 = [[] for _ in range(n+2)]
    for i, (l, r) in enumerate(zip(left, right)):
        cur = n
        d = n
        if r < n:
            d = r - i
            cur = r
        if l >= 0 and i - l < d:
            cur = l
        g2[cur+1].append(i+1)
    # print(g2)
    hld = HLD(g2,n+1)
    size = hld.size
    dfn = hld.dfn
    dep = hld.dep
    # print(dep)
    zkw = ZKW([inf]*(n+2), min, inf)

    route = []
    ans = [0]*(n+2)
    def dfs(u):
        route.append(u)
        pre = 0
        if len(route) >= k+2:
            pre = zkw.get(dfn[route[-k - 2]])
            # print(route,-k-1,route[-k - 2])
            zkw.set(dfn[route[-k-2]],inf)
        p = zkw.query(dfn[u]+1,dfn[u]+size[u])
        # print(p)
        if p - dep[u] <= k:
            ans[u] = 1
        # print(u,route,zkw)
        # print(u,dfn[u],dep[u])
        zkw.set(dfn[u],dep[u])
        # print( zkw)
        for v in g1[u]:
            dfs(v)

        zkw.set(dfn[u],inf)
        if len(route) >= k+2:
            zkw.set(dfn[route[-k - 2]], pre)

        route.pop()


    dfs(n+1)

    print(*ans[1:-1],sep='')



solve()

sys.stdout.close()
