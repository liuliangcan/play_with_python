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


def main():
    T, = RI()
    for _ in range(T):
        n, m = RI()
        g = [[] for _ in range(n)]
        for _ in range(m):
            u, v, w = RI()
            if w >= 0:
                g[v - 1].append((u - 1, w))
            g[u - 1].append((v - 1, w))

        if Spfa(g, 0).has_negative_circle():
            print('YES')
        else:
            print('NO')


if __name__ == '__main__':
    # testcase 2个字段分别是input和output
    test_cases = (
        (
            """2
3 4
1 2 2
1 3 4
2 3 1
3 1 -3
3 3
1 2 3
2 3 4
3 1 -8""", """NO
YES
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
