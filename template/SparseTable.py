"""稀疏表，O(nlgn)初始化，O(1)查询"""
from operator import or_


class SparseTable:
    def __init__(self, data: list, func=or_):
        # 稀疏表，O(nlgn)预处理，O(1)查询区间最值/或和/gcd/lcm
        # 下标从0开始
        self.func = func
        self.st = st = [list(data)]
        i, N = 1, len(st[0])
        while 2 * i <= N + 1:
            pre = st[-1]
            st.append([func(pre[j], pre[j + i]) for j in range(N - 2 * i + 1)])
            i <<= 1

    def query(self, begin: int, end: int):  # 查询闭区间[begin, end]的最大值
        lg = (end - begin + 1).bit_length() - 1
        return self.func(self.st[lg][begin], self.st[lg][end - (1 << lg) + 1])


"""
https://www.cnblogs.com/-Ackerman/p/11387105.html
https://www.lanqiao.cn/problems/17002/learning/?contest_id=174
class SparseTable2D:
    def __init__(self,data,func=max):
        self.func = func
        self.st = st = [[[[1]]]]
"""



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
