

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
