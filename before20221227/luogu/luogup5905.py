import collections
import sys
from collections import *
from contextlib import redirect_stdout
from itertools import *
from math import sqrt, inf
from array import *
from functools import lru_cache
import heapq
import bisect
import random
import io, os
from bisect import *

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda x: sys.stderr.write(f'{str(x)}\n')


class Spfa:
    """
    单源最短路，支持负权，复杂度O(m*n)
    """

    def __init__(self, g, start, n=None, INF=None):
        self.n = len(g) if n is None else n
        self.g = g
        self.start = start
        self.INF = INF if INF is not None else inf

    def has_negative_circle(self):
        """
        判断是否存在负环，即权为负的环，因为如果存在负环，路径每经过一次这个环就减小，永远出不来。
        判断入队的点n次以上即出不来了，因为bellman-ford可知最多松弛n-1次就应该有答案
        :return:
        """
        dis, g, n = [self.INF] * self.n, self.g, self.n  # 初始化距离数据为全inf
        dis[self.start] = 0  # 源到自己距离0
        q = deque([(0, self.start)])
        cnt = [0] * n
        while q:
            c, u = q.popleft()  # 当前点的最短路
            cnt[u] += 1
            if cnt[u] >= n:
                return True  # 有个点入队了n次以上，说明永远也结束不了，存在负环
            if c > dis[u]: continue
            for v, w in g[u]:  # 用u松弛它的邻居
                d = c + w
                if d < dis[v]:  # 可以松弛

                    dis[v] = d
                    q.append((d, v))
        return False  # 可以结束，不存在负环

    def safe_dist_by_list_g_0_indexed(self):
        """
        :return: 如果有负环返回空，否则正常返回距离数组
        """
        dis, g, n = [self.INF] * self.n, self.g, self.n  # 初始化距离数据为全inf
        dis[self.start] = 0  # 源到自己距离0
        q = deque([(0, self.start)])
        cnt = [0] * n
        while q:
            c, u = q.popleft()  # 当前点的最短路
            cnt[u] += 1
            if cnt[u] >= n:
                return []  # 有个点入队了n次以上，说明永远也结束不了，存在负环
            if c > dis[u]: continue
            for v, w in g[u]:  # 用u松弛它的邻居
                d = c + w
                if d < dis[v]:  # 可以松弛

                    dis[v] = d
                    q.append((d, v))
        return dis  # 可以结束，不存在负环

    def unsafe_dist_by_list_g_0_indexed(self):
        """
        基于g是从0~n-1表示节点的图
        :return: 距离数组代表start点到每个点的最短路
        """
        dis, g = [self.INF] * self.n, self.g  # 初始化距离数据为全inf
        dis[self.start] = 0  # 源到自己距离0
        q = deque([(0, self.start)])
        while q:
            c, u = q.popleft()  # 当前点的最短路
            if c > dis[u]: continue
            for v, w in g[u]:  # 用u松弛它的邻居
                d = c + w
                if d < dis[v]:  # 可以松弛
                    dis[v] = d
                    q.append((d, v))
        return dis  # 距离数组

    def unsafe_dist_by_dict_g(self):
        """优先用defaultdict版本，卡性能再考虑这个
        基于二重dict的图;注意字典图的话，两点之间可能存在重边，可能需要判断丢弃
        由于有的最短路题目是矩阵，因此一个点是用(x,y)坐标表示的，这时用数组存图就不太方便，改用defaultdict。
        :return: 距离字典:{u:dist}，注意，如果不在这个字典里，则不可达；外侧查询的话可能需要dis.get(u,inf);其实可以用defaultdict来存，但是效率低一些。
        """
        dis, g = {self.start: 0}, self.g  # 初始化距离字典
        INF = self.INF
        q = deque([(0, self.start)])
        while q:
            c, u = q.popleft()
            if c > dis.get(u, INF): continue
            for v, w in g[u].items():
                d = c + w
                if d < dis.get(v, INF):
                    dis[v] = d
                    q.append((d, v))
        return dis

    def unsafe_dist_by_default_dict_g(self):
        """
        基于二重dict的图;注意字典图的话，两点之间可能存在重边，可能需要判断丢弃
        由于有的最短路题目是矩阵，因此一个点是用(x,y)坐标表示的，这时用数组存图就不太方便，改用defaultdict。
        :return: 距离字典:defaultdict({u:dist})，注意，速度比上个函数慢一点，但是不易出错，因为可以初始化不可达为inf
        """
        dis, g = defaultdict(lambda: self.INF), self.g  # 初始化距离字典
        dis[self.start] = 0
        q = deque([(0, self.start)])
        while q:
            c, u = q.popleft()
            if c > dis[u]: continue

            for v, w in g[u].items():
                d = c + w
                if d < dis[v]:
                    dis[v] = d
                    q.append((d, v))
        return dis

    def unsafe_dist(self):
        """根据g的类型自动判断是不是用下标代替节点，速度快一点"""
        if isinstance(self.g, list):
            return self.unsafe_dist_by_list_g_0_indexed()
        return self.unsafe_dist_by_default_dict_g()


class Dijkstra:
    """
    堆优化版dijkstra单源最短路，求从start到所有点的最短路，边权不能为负；时间复杂度nlogn
    其中INF可以自己定义，用来表示无法到达，默认是inf
    """

    def __init__(self, g, start, n=None, INF=None):
        self.n = len(g) if n is None else n
        self.g = g
        self.start = start
        self.INF = INF if INF is not None else inf

    def dist_by_list_g_0_indexed(self):
        """
        基于g是从0~n-1表示节点的图
        :return: 距离数组代表start点到每个点的最短路
        """
        dis, g = [self.INF] * self.n, self.g  # 初始化距离数据为全inf
        dis[self.start] = 0  # 源到自己距离0
        q = [(0, self.start)]  # 优先队列
        while q:
            c, u = heapq.heappop(q)  # 当前点的最短路
            if c > dis[u]: continue  # 这步巨量优化很重要:u可以从上一层多个点转移而来，队列中将同时存在多个u的情况，但只有c最小的那个有意义，其他跳过。
            for v, w in g[u]:  # 用u松弛它的邻居
                d = c + w
                if d < dis[v]:  # 可以松弛
                    dis[v] = d
                    heapq.heappush(q, (d, v))
        return dis  # 距离数组

    def dist_by_dict_g(self):
        """
        基于二重dict的图;注意字典图的话，两点之间可能存在重边，可能需要判断丢弃
        由于有的最短路题目是矩阵，因此一个点是用(x,y)坐标表示的，这时用数组存图就不太方便，改用defaultdict。
        :return: 距离字典:{u:dist}，注意，如果不在这个字典里，则不可达；外侧查询的话可能需要dis.get(u,inf);其实可以用defaultdict来存，但是效率低一些。
        """
        dis, g = {self.start: 0}, self.g  # 初始化距离数组

        q = [(0, self.start)]
        while q:
            c, u = heapq.heappop(q)
            if c > dis.get(u, inf): continue
            for v, w in g[u].items():
                d = c + w
                if d < dis.get(v, inf):
                    dis[v] = d
                    heapq.heappush(q, (d, v))
        return dis

    def dist_by_default_dict_g(self):
        """优先用defaultdict版本，卡性能再考虑这个
        基于二重dict的图;注意字典图的话，两点之间可能存在重边，可能需要判断丢弃
        由于有的最短路题目是矩阵，因此一个点是用(x,y)坐标表示的，这时用数组存图就不太方便，改用defaultdict。
        :return: 距离字典:defaultdict({u:dist})，注意，速度比上个函数慢一点，但是不易出错，因为可以初始化不可达为inf
        """
        dis, g = defaultdict(lambda: self.INF), self.g  # 初始化距离字典
        dis[self.start] = 0
        q = [(0, self.start)]
        while q:
            c, u = heapq.heappop(q)
            if c > dis[u]: continue
            for v, w in g[u].items():
                d = c + w
                if d < dis[v]:
                    dis[v] = d
                    heapq.heappush(q, (d, v))
        return dis

    def dist(self):
        """根据g的类型自动判断是不是用下标代替节点，速度快一点"""
        if isinstance(self.g, list):
            return self.dist_by_list_g_0_indexed()
        return self.dist_by_default_dict_g()


class Johnson:
    """
    支持负权的全源最短路，复杂度M*NlogN
    建立超级源点n，连接每个点，边权为0，然后SPFA对n求最短路,记为h（O(N*M)）
    修正原图的(u,v,w)边权为w+h[u]-h[v]，这里类似前缀和/差分。用势能考虑
    然后以每个点为起点，求n次最短路Dijkstra。最后把求得的最短路再修正回来(减去势能)
    不支持INF参数，因为可能计算的最短路恰好等于INF，再修正就有问题；
    - 这里只有safe版本，即顺便检查是否有负环；如果没有负边，那可以手写n次Dijkstra。
    - 这么看难道普通Dijkstra也可以处理负边问题吗？是的，但是要先用SPFA预处理，那还不如直接SPFA
    """
    def __init__(self, g, n=None):
        self.n = len(g) if n is None else n
        self.g = g

    def safe_dist(self):
        """
        如果存在负环返回空数组；否则返回二维数组dist[i][j]代表i到j的最短路
        :return:
        """
        g, n = self.g + [[]], self.n

        for u in range(n):  # 建立超级源点n,到达所有点，w=0
            g[n].append((u, 0))
        h = Spfa(g, n).safe_dist_by_list_g_0_indexed()  # 对n点求最短路，如果有负环就返回
        if not h: return h  # 存在负环，别聊了
        g.pop()  # 删除超级源点

        for u in range(n):  # 把图中边权修正为w+h[u]-h[v]
            p, g[u] = g[u], []
            for v, w in p:
                g[u].append((v, w + h[u] - h[v]))
        ans = []
        for u in range(n):
            dis = Dijkstra(g, u).dist()
            ans.append([d + h[v] - h[u] for v, d in enumerate(dis)])  # 把最短路修正回来
        return ans


def main():
    n, m = RI()
    g = [[] for _ in range(n )]
    for _ in range(m):
        u, v, w = RI()
        g[u - 1].append((v - 1, w))
    INF = 10 ** 9
    dises = Johnson(g).safe_dist()
    # DEBUG(dises)
    if not dises: return print(-1)
    ans = []
    for u, dis in enumerate(dises):
        ans.append(sum(j * d if d < inf else j*INF for j, d in enumerate(dis,start=1)))
    print(*ans, sep='\n')


if __name__ == '__main__':
    # testcase 2个字段分别是input和output
    test_cases = (
        (
            """5 7
1 2 4
1 4 10
2 3 7
4 5 3
4 2 -2
3 4 -3
5 3 4""", """128
1000000072
999999978
1000000026
1000000014
"""
        ),
        (
            """5 5
1 2 4
3 4 9
3 4 -3
4 5 3
5 3 -2""", """-1
"""
        ),
    )
    if os.path.exists('test.test'):
        total_result = 'ok!'
        for i, (in_data, result) in enumerate(test_cases):
            result = result.strip()
            with io.StringIO(in_data.strip()) as buf_in:
                RI = lambda: map(int, buf_in.readline().split())
                RS = lambda: buf_in.readline().strip().split()
                with io.StringIO() as buf_out, redirect_stdout(buf_out):
                    main()
                    output = buf_out.getvalue().strip()
                if output == result:
                    print(f'case{i}, result={result}, output={output}, ---ok!')
                else:
                    print(f'case{i}, result={result}, output={output}, ---WA!---WA!---WA!')
                    total_result = '---WA!---WA!---WA!'
        print('\n', total_result)
    else:
        main()
