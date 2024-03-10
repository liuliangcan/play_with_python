import sys
import random
from types import GeneratorType
import bisect
import io, os
from bisect import *
from collections import *
from contextlib import redirect_stdout
from itertools import *
from array import *
from functools import lru_cache, reduce
from heapq import *
from math import sqrt, gcd, inf, log2

# if not sys.version.startswith('3.5.3'):  # ACW没有comb
#     from math import comb

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')
# print = lambda d: sys.stdout.write(str(d) + "\n")  # 打开可以快写，但是无法使用print(*ans,sep=' ')这种语法,需要print(' '.join(map(str, p)))，确实会快。

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 右下左上
DIRS8 = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]  # →↘↓↙←↖↑↗
RANDOM = random.randrange(2 ** 62)
MOD = 10 ** 9 + 7
# MOD = 998244353
PROBLEM = """https://www.lanqiao.cn/problems/17002/learning/?contest_id=174
"""


class PreSum2d:
    # 二维前缀和(支持加法和异或)，只能离线使用，用n*m时间预处理，用O1查询子矩阵的和；op=0是加法，op=1是异或
    def __init__(self, g, op=0):
        m, n = len(g), len(g[0])
        self.op = op
        self.p = p = [[0] * (n + 1) for _ in range(m + 1)]
        if op == 0:
            for i in range(m):
                for j in range(n):
                    p[i + 1][j + 1] = p[i][j + 1] + p[i + 1][j] - p[i][j] + g[i][j]
        elif op == 1:
            for i in range(m):
                for j in range(n):
                    p[i + 1][j + 1] = p[i][j + 1] ^ p[i + 1][j] ^ p[i][j] ^ g[i][j]

    # O(1)时间查询闭区间左上(a,b),右下(c,d)矩形部分的数字和。
    def sum_square(self, a, b, c, d):
        if self.op == 0:
            return self.p[c + 1][d + 1] + self.p[a][b] - self.p[a][d + 1] - self.p[c + 1][b]
        elif self.op == 1:
            return self.p[c + 1][d + 1] ^ self.p[a][b] ^ self.p[a][d + 1] ^ self.p[c + 1][b]


class MatrixMonoQue:
    """在矩阵上跑横纵两次单调队列
    固定子矩阵大小(m1,n1)的情况下，返回size为[m-m1+1,n-n1+1]的答案矩阵，
    ans[i][j]表示原矩阵的子矩阵[i,j,i+m1-1,j+n1-1]的极值，换句话说，每个子矩阵的极值储存在左上角
    """
    def __init__(self, g):
        self.g = g
        self.m, self.n = len(g), len(g[0])

    def get_min_mat(self, m1, n1):
        '''获取每个大小为[m1,n1]的子块最小值，相当于储存在左上角'''
        g = self.g
        m, n = len(g), len(g[0])
        mn = [[0] * (n - n1 + 1) for _ in range(m)]
        for i, row in enumerate(g):
            q = deque()
            for j, v in enumerate(row):
                while q and row[q[-1]] >= v:
                    q.pop()
                q.append(j)
                if j - q[0] + 1 > n1:
                    q.popleft()
                if j >= n1 - 1:
                    mn[i][j - n1 + 1] = row[q[0]]

        for j in range(n - n1 + 1):
            q = deque()
            for i in range(m):
                v = mn[i][j]
                while q and mn[q[-1]][j] >= v:
                    q.pop()
                q.append(i)
                if i - q[0] + 1 > m1:
                    q.popleft()
                if i >= m1 - 1:
                    mn[i - m1 + 1][j] = mn[q[0]][j]
        return mn[:m - m1 + 1 + 1]

    def get_max_mat(self, m1, n1):
        '''获取每个大小为[m1,n1]的子块最大值，相当于储存在左上角'''
        g = self.g
        m, n = len(g), len(g[0])
        mx = [[0] * (n - n1 + 1) for _ in range(m)]
        for i, row in enumerate(g):
            q = deque()
            for j, v in enumerate(row):
                while q and row[q[-1]] <= v:
                    q.pop()
                q.append(j)
                if j - q[0] + 1 > n1:
                    q.popleft()
                if j >= n1 - 1:
                    mx[i][j - n1 + 1] = row[q[0]]

        for j in range(n - n1 + 1):
            q = deque()
            for i in range(m):
                v = mx[i][j]
                while q and mx[q[-1]][j] <= v:
                    q.pop()
                q.append(i)
                if i - q[0] + 1 > m1:
                    q.popleft()
                if i >= m1 - 1:
                    mx[i - m1 + 1][j] = mx[q[0]][j]
        return mx[:m - m1 + 1 + 1]


#       ms
def solve():
    m, n, m1, n1 = RI()
    g = []
    for _ in range(m):
        g.append(RILST())
    ps = PreSum2d(g)
    mq = MatrixMonoQue(g)
    mn = mq.get_min_mat(m1,n1)
    mx = mq.get_max_mat(m1,n1)

    ans = -inf
    for i in range(m - m1 + 1):
        for j in range(n - n1 + 1):
            ans = max(ans, ps.sum_square(i, j, i + m1 - 1, j + n1 - 1) * (mx[i][j] - mn[i][j]))
    print(ans)


def solve2():
    m, n, m1, n1 = RI()
    g = []
    for _ in range(m):
        g.append(RILST())
    ps = PreSum2d(g)
    mn = [[0] * (n - n1 + 1) for _ in range(m)]
    mx = [[0] * (n - n1 + 1) for _ in range(m)]
    for i, row in enumerate(g):
        q1, q2 = deque(), deque()
        for j, v in enumerate(row):
            while q1 and row[q1[-1]] >= v:
                q1.pop()
            q1.append(j)
            if j - q1[0] + 1 > n1:
                q1.popleft()
            while q2 and row[q2[-1]] <= v:
                q2.pop()
            q2.append(j)
            if j - q2[0] + 1 > n1:
                q2.popleft()
            if j >= n1 - 1:
                mn[i][j - n1 + 1] = row[q1[0]]
                mx[i][j - n1 + 1] = row[q2[0]]

    for j in range(n - n1 + 1):
        q1, q2 = deque(), deque()
        for i in range(m):
            v = mn[i][j]
            while q1 and mn[q1[-1]][j] >= v:
                q1.pop()
            q1.append(i)
            if i - q1[0] + 1 > m1:
                q1.popleft()
            v = mx[i][j]
            while q2 and mx[q2[-1]][j] <= v:
                q2.pop()
            q2.append(i)
            if i - q2[0] + 1 > m1:
                q2.popleft()
            if i >= m1 - 1:
                mn[i - m1 + 1][j] = mn[q1[0]][j]
                mx[i - m1 + 1][j] = mx[q2[0]][j]
    mn = mn[:m - m1 + 1 + 1]
    mx = mx[:m - m1 + 1 + 1]

    ans = -inf
    for i in range(m - m1 + 1):
        for j in range(n - n1 + 1):
            ans = max(ans, ps.sum_square(i, j, i + m1 - 1, j + n1 - 1) * (mx[i][j] - mn[i][j]))
    print(ans)


class SparseTable2D:
    def __init__(self, matrix, method="max"):
        m, n = len(matrix), len(matrix[0])
        a, b = int(log2(m)) + 1, int(log2(n)) + 1

        if method == "max":
            self.fun = max
        elif method == "min":
            self.fun = min
        elif method == "gcd":
            self.fun = self.gcd
        elif method == "lcm":
            self.fun = min
        elif method == "or":
            self.fun = self._or
        else:
            self.fun = self._and

        self.dp = [[[[0 for _ in range(b)] for _ in range(a)] for _ in range(n)] for _ in range(m)]

        for i in range(a):
            for j in range(b):
                for x in range(m - (1 << i) + 1):
                    for y in range(n - (1 << j) + 1):
                        if i == 0 and j == 0:
                            self.dp[x][y][i][j] = matrix[x][y]
                        elif i == 0:
                            self.dp[x][y][i][j] = self.fun([self.dp[x][y][i][j - 1],
                                                            self.dp[x][y + (1 << (j - 1))][i][j - 1]])
                        elif j == 0:
                            self.dp[x][y][i][j] = self.fun([self.dp[x][y][i - 1][j],
                                                            self.dp[x + (1 << (i - 1))][y][i - 1][j]])
                        else:
                            self.dp[x][y][i][j] = self.fun([self.dp[x][y][i - 1][j - 1],
                                                            self.dp[x + (1 << (i - 1))][y][i - 1][j - 1],
                                                            self.dp[x][y + (1 << (j - 1))][i - 1][j - 1],
                                                            self.dp[x + (1 << (i - 1))][y + (1 << (j - 1))][i - 1][
                                                                j - 1]])
        return

    @staticmethod
    def max(args):
        return reduce(max, args)

    @staticmethod
    def min(args):
        return reduce(min, args)

    @staticmethod
    def gcd(args):
        return reduce(gcd, args)

    @staticmethod
    def lcm(args):
        return reduce(lcm, args)

    @staticmethod
    def _or(args):
        return reduce(or_, args)

    @staticmethod
    def _and(args):
        return reduce(and_, args)

    def query(self, x, y, x1, y1):
        # index start from 0 and left up corner is (x, y) and right down corner is (x1, y1)
        k = int(log2(x1 - x + 1))
        p = int(log2(y1 - y + 1))
        ans = self.fun([self.dp[x][y][k][p],
                        self.dp[x1 - (1 << k) + 1][y][k][p],
                        self.dp[x][y1 - (1 << p) + 1][k][p],
                        self.dp[x1 - (1 << k) + 1][y1 - (1 << p) + 1][k][p]])
        return ans


def solve1():
    m, n, m1, n1 = RI()
    g = []
    for _ in range(m):
        g.append(RILST())
    ps = PreSum2d(g)
    mx = SparseTable2D(g, 'max')
    mn = SparseTable2D(g, 'min')

    # print(mn)
    # print(mx)
    ans = -inf
    for i in range(m - m1 + 1):
        for j in range(n - n1 + 1):
            ans = max(ans, ps.sum_square(i, j, i + m1 - 1, j + n1 - 1) * (
                    mx.query(i, j, i + m1 - 1, j + n1 - 1) - mn.query(i, j, i + m1 - 1, j + n1 - 1)))
    print(ans)


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
