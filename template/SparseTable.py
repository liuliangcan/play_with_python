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

