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

    def dist_by_list_g_0_indexed(self):
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

    def dist_by_dict_g(self):
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

    def dist_by_default_dict_g(self):
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

    def dist(self):
        """根据g的类型自动判断是不是用下标代替节点，速度快一点"""
        if isinstance(self.g, list):
            return self.dist_by_list_g_0_indexed()
        return self.dist_by_default_dict_g()


def main():
    n, m, s = RI()

    g = collections.defaultdict(dict)
    for _ in range(m):
        u, v, w = RI()
        a, b = u - 1, v - 1
        if b in g[a]:  # 在这wa了很多次，字典形式的图要处理重边
            g[a][b] = min(g[a][b], w)
        else:
            g[a][b] = w

    dis = Spfa(g, s - 1, INF=2 ** 31 - 1).dist()
    ans = [0] * n
    for i in range(n):
        ans[i] = dis[i]
    print(*ans)


# def main():
#     n, m, s = RI()
#     g = [[] for _ in range(n)]
#     for _ in range(m):
#         u, v, w = RI()
#         g[u - 1].append((v - 1, w))
#
#     dis = Spfa(g, s - 1).dist()
#     for i, v in enumerate(dis):
#         if v == inf:
#             dis[i] = 2 ** 31 - 1
#     print(*dis)


if __name__ == '__main__':
    # testcase 2个字段分别是input和output
    test_cases = (
        (
            """4 6 1
1 2 2
2 3 2
2 4 1
1 3 5
3 4 3
1 4 4""", """0 2 4 3
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
