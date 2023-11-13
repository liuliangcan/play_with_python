"""atc上抄的板子，但是常数貌似挺大，tle了
https://codeforces.com/problemset/problem/282/E
"""
class BinaryTrie:
    """
    Reference:
     - https://atcoder.jp/contests/arc028/submissions/19916627
     - https://judge.yosupo.jp/submission/35057
    """

    __slots__ = (
        "max_log",
        "x_end",
        "v_list",
        "multiset",
        "add_query_count",
        "add_query_limit",
        "edges",
        "size",
        "is_end",
        "max_v",
        "lazy",
    )

    def __init__(
            self,
            max_log: int = 60,  # 字典树最大深度，取决于值域
            allow_multiple_elements: bool = True,  # 是否允许重复数值
            add_query_limit: int = 10 ** 5,  # 允许添加多少次数字（试了下1e6会mle
    ):
        self.max_log = max_log  # 最大深度
        self.x_end = 1 << max_log  # 这个深度下允许的值域最大值
        self.v_list = [0] * (max_log + 1)  # 当前插入数字的路径
        self.multiset = allow_multiple_elements
        self.add_query_count = 0  # 计数添加了多少次，感觉没用
        self.add_query_limit = add_query_limit  # 最多允许这么多次访问，assert注释了
        n = max_log * add_query_limit + 1  # 开这么长的数组
        self.edges = [-1] * (2 * n)
        self.size = [0] * n
        self.is_end = [0] * n
        self.max_v = 0
        self.lazy = 0  # 用于整棵树异或

    def add(self, x: int):
        # assert 0 <= x < self.x_end
        # assert 0 <= self.add_query_count < self.add_query_limit
        x ^= self.lazy
        v = 0
        for i in range(self.max_log - 1, -1, -1):
            d = (x >> i) % 2
            if self.edges[2 * v + d] == -1:
                self.max_v += 1
                self.edges[2 * v + d] = self.max_v
            v = self.edges[2 * v + d]
            self.v_list[i] = v
        if self.multiset or self.is_end[v] == 0:  # 如果允许重复插入，则计数
            self.is_end[v] += 1
            for v in self.v_list:  # 记录这个位置被路过的次数
                self.size[v] += 1
        self.add_query_count += 1

    def find_max_xor(self, x):
        """找到集合里所有数据异或x的最大值"""
        x ^= self.lazy
        v = 0
        ret = 0
        for i in range(self.max_log - 1, -1, -1):
            d = x >> i & 1
            if self.edges[(v << 1) | (d ^ 1)] != -1 and  self.size[self.edges[(v << 1) | (d ^ 1)]]:  # 对面有，则这层可以是1，去对面
                ret |= 1 << i
                v = self.edges[(v << 1) | (d ^ 1)]
            else:
                v = self.edges[(v << 1) | d]
        return ret

    def discard(self, x: int):
        # 移除一个x
        if not 0 <= x < self.x_end:
            return
        x ^= self.lazy
        v = 0
        for i in range(self.max_log - 1, -1, -1):
            d = (x >> i) % 2
            if self.edges[2 * v + d] == -1:
                return
            v = self.edges[2 * v + d]
            self.v_list[i] = v
        if self.is_end[v] > 0:
            self.is_end[v] -= 1
            for v in self.v_list:
                self.size[v] -= 1

    def erase(self, x: int, count: int = -1):
        # 移除count个x；如果count==-1，则全部移除
        # assert -1 <= count
        if not 0 <= x < self.x_end:
            return
        x ^= self.lazy
        v = 0
        for i in range(self.max_log - 1, -1, -1):
            d = (x >> i) % 2
            if self.edges[2 * v + d] == -1:
                return
            v = self.edges[2 * v + d]
            self.v_list[i] = v
        if count == -1 or self.is_end[v] < count:
            count = self.is_end[v]
        if self.is_end[v] > 0:
            self.is_end[v] -= count
            for v in self.v_list:
                self.size[v] -= count

    def count(self, x: int) -> int:  #
        # 检查有几个x
        if not 0 <= x < self.x_end:
            return 0
        x ^= self.lazy
        v = 0
        for i in range(self.max_log - 1, -1, -1):
            d = (x >> i) % 2
            if self.edges[2 * v + d] == -1:
                return 0
            v = self.edges[2 * v + d]
        return self.is_end[v]

    def bisect_left(self, x: int) -> int:
        # 找第一个大于等于x数的下标；也可以说是找有几个数比x小
        if x < 0:
            return 0
        if self.x_end <= x:
            return len(self)
        v = 0
        ret = 0
        for i in range(self.max_log - 1, -1, -1):
            d = (x >> i) % 2
            l = (self.lazy >> i) % 2
            lc = self.edges[2 * v]
            rc = self.edges[2 * v + 1]
            if l == 1:
                lc, rc = rc, lc
            if d:
                if lc != -1:
                    ret += self.size[lc]
                if rc == -1:
                    return ret
                v = rc
            else:
                if lc == -1:
                    return ret
                v = lc
        return ret

    def bisect_right(self, x: int) -> int:
        # 找第一个比x大的数的下标
        return self.bisect_left(x + 1)

    def index(self, x: int) -> int:
        if x not in self:
            raise ValueError(f"{x} is not in BinaryTrie")
        return self.bisect_left(x)

    def find(self, x: int) -> int:
        # 找x是否在树里，不在返回-1；在返回下标
        if x not in self:
            return -1
        return self.bisect_left(x)

    def kth_elem(self, k: int) -> int:
        # 计算第k小的值，其中k是0-index
        if k < 0:
            k += self.size[0]
        # assert 0 <= k < self.size[0]
        v = 0
        ret = 0
        for i in range(self.max_log - 1, -1, -1):
            l = (self.lazy >> i) % 2
            lc = self.edges[2 * v]
            rc = self.edges[2 * v + 1]
            if l == 1:
                lc, rc = rc, lc
            if lc == -1:
                v = rc
                ret |= 1 << i
                continue
            if self.size[lc] <= k:
                k -= self.size[lc]
                v = rc
                ret |= 1 << i
            else:
                v = lc
        return ret

    def minimum(self) -> int:
        # 返回树里最小的值
        return self.kth_elem(0)

    def maximum(self) -> int:
        # 返回树里最大的值
        return self.kth_elem(-1)

    def xor_all(self, x: int):
        # 把整棵树上所有值都异或x
        # assert 0 <= x < self.x_end
        self.lazy ^= x

    def __iter__(self):
        q = [(0, 0)]
        for i in range(self.max_log - 1, -1, -1):
            l = (self.lazy >> i) % 2
            nq = []
            for v, x in q:
                lc = self.edges[2 * v]
                rc = self.edges[2 * v + 1]
                if l == 1:
                    lc, rc = rc, lc
                if lc != -1:
                    nq.append((lc, 2 * x))
                if rc != -1:
                    nq.append((rc, 2 * x + 1))
            q = nq
        for v, x in q:
            for _ in range(self.is_end[v]):
                yield x

    def __str__(self):
        prefix = "BinaryTrie("
        content = list(map(str, self))
        suffix = ")"
        if content:
            content[0] = prefix + content[0]
            content[-1] = content[-1] + suffix
        else:
            content = [prefix + suffix]
        return ", ".join(content)

    def __getitem__(self, k):
        return self.kth_elem(k)

    def __contains__(self, x: int) -> bool:
        return bool(self.count(x))

    def __len__(self):
        return self.size[0]

    def __bool__(self):
        return bool(len(self))

    def __ixor__(self, x: int):
        self.xor_all(x)
        return self



class Solution:
        def countPairs(self, nums: List[int], low: int, high: int) -> int:
            n = len(nums)
            max_log = max(nums).bit_length()
            bt = BinaryTrie(add_query_limit=n, max_log=max_log, allow_multiple_elements=True)
            ans = 0
            for num in nums:
                bt.xor_all(num)
                ans += bt.bisect_right(high) - bt.bisect_left(low)
                bt.xor_all(num)
                bt.add(num)
            return ans
