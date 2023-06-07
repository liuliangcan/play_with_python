from itertools import accumulate


class DiffArr:
    """一维差分
    原数组是差分数组的前缀和，其中d[0]=a[0]-0,d[i]=a[i]-a[i-1].原数组a range_add(l,r,v)等价于d[l]+=v,d[r+1]-=v,因此通常d长度开n+1(但几乎不需要访问d[n])
        众所周知前缀和是离线的，因此每次随机查询原数组时，都要从0~i累加一遍，这是O(n)的。
        若要每个位置都查询，那就是O(n^2)。
            但如果查询是顺序的，那么前缀和就可以遍历时同时计算(复用前边的前缀和状态)，单次查询均摊为O(1)。
    - 因此使用此模板请保证查询是顺序的
    """
    def __init__(self, n):
        self.d = [0] * (n + 1)  # 通常多申请一位就不用判断特判位置n
        self.cur_idx = -1  # 当前前缀和累计到哪了
        self.cur_s = 0  # 当前位置累计的前缀和（即原数组当前位置上的值
        self.n = n

    def query_point(self, i):
        """查询原数组位置i上的值a[i]
        i:0-index
        注意，若查询的i是顺序的，那么cur_idx和cur_s将一直向后累计，均摊复杂度为O(1)
        否则，若出现i<cur_idx，那么将从0开始重新累计，复杂度为O(n)。若有这种需求请优先考虑使用BIT等其它RUPQ的数据结构
        """
        # assert self.cur_idx <= i  # 理论上来说不可以,会导致复杂度变成O(n)
        if self.cur_idx > i:  # 理论上来说不可以,会导致复杂度变成O(n)
            self.cur_idx = -1
            self.cur_s = 0
        while self.cur_idx < i:
            self.cur_idx += 1
            self.cur_s += self.d[self.cur_idx]
        return self.cur_s

    def add_interval(self, l, r, v):
        """给原数组闭区间[l,r]上的数全部+=v，注意0-indexed"""
        if l <= self.cur_idx <= r:  # 如果修改的位置恰好包含cur_idx那么需要给前缀和增加
            self.cur_s += v
        self.d[l] += v
        if r < self.n:  # 由于d开了n+1长度，有时不需要，但有的题增加的区间右端点可能超过n，那还是在这里加特判吧
            self.d[r + 1] -= v

    def get_a(self):
        """获取原数组"""
        return list(accumulate(self.d))[:-1]


# a = [2,3,3,1,]
# n = len(a)
# d = DiffArr(n)
# for i,v in enumerate(a):
#     d.add_interval(i,i,v)
# print(d.get_a())