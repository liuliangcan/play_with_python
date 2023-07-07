# Problem: E. Sausage Maximization
# Contest: Codeforces - Codeforces Round 173 (Div. 2)
# URL: https://codeforces.com/problemset/problem/282/E
# Memory Limit: 256 MB
# Time Limit: 2000 ms

import sys

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')
# print = lambda d: sys.stdout.write(str(d) + "\n")  # 打开可以快写，但是无法使用print(*ans,sep=' ')这种语法,需要print(' '.join(map(str, p)))，确实会快。

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 右下左上
DIRS8 = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0),
         (-1, 1)]  # →↘↓↙←↖↑↗
MOD = 10 ** 9 + 7
# MOD = 998244353
PROBLEM = """https://codeforces.com/problemset/problem/282/E

输入 n(1≤n≤1e5) 和长为 n 的数组 a(0≤a[i]≤1e12)。
选择 a 的一个前缀（可以为空）和一个后缀（可以为空），要求前缀后缀不相交。
输出所选数字的异或和的最大值。
输入 
2
1 2
输出 3

输入
3
1 2 3
输出 3

输入 
2
1000 1000
输出 1000
"""


class TrieXor:
    def __init__(self, nums=None, bit_len=32):
        # 01字典树，用来处理异或最值问题，本模板只处理数字最低的31位
        # 用nums初始化字典树，可以为空
        self.tree = {}
        self.bit_len = bit_len
        if nums:
            for a in nums:
                self.insert(a)

    def insert(self, num):
        # 01字典树插入一个数字num,只会处理最低bit_len位。
        cur = self.tree
        for i in range(self.bit_len - 1, -1, -1):
            nxt = (num >> i) & 1
            if nxt not in cur:
                cur[nxt] = {}
            cur = cur[nxt]

    def find_max_xor_num(self, num):
        # 计算01字典树里任意数字异或num的最大值,只会处理最低bit_len位。
        # 贪心的从高位开始处理，显然num的某位是0，对应的优先应取1；相反同理
        cur = self.tree
        ret = 0
        cur.items()
        for i in range(self.bit_len - 1, -1, -1):
            if (num >> i) & 1 == 0:  # 如果本位是0，那么取1才最大；取不到1才取0
                if 1 in cur:
                    cur = cur[1]
                    ret += ret + 1
                else:
                    cur = cur.get(0, {})
                    ret <<= 1
            else:
                if 0 in cur:
                    cur = cur[0]
                    ret += ret + 1
                else:
                    cur = cur.get(1, {})
                    ret <<= 1
        return ret


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
            if self.edges[(v << 1) | (d ^ 1)] != -1 and self.size[self.edges[(v << 1) | (d ^ 1)]]:  # 对面有，则这层可以是1，去对面
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


# 带删除 934ms
def solve1():
    n, = RI()
    a = RILST()
    trie = BinaryTrie(40)
    trie.add(0)
    ans = 0
    pre = [0]

    for v in a:
        pre.append(pre[-1] ^ v)
        trie.add(pre[-1])
    p = 0
    for i in range(n - 1, -1, -1):
        p ^= a[i]
        trie.discard(pre[i - 1])
        ans = max(ans, p, trie.find_max_xor(p))
    print(ans)


# 686ms
def solve():
    n, = RI()
    a = RILST()
    trie = BinaryTrie(40, False)
    ans = p = 0
    for v in a:
        p ^= v
        ans = max(ans, p)
        trie.add(p)
    p = 0
    for v in a[::-1]:
        p ^= v
        ans = max(ans, p, trie.find_max_xor(p))
    print(ans)


# 764ms
def solve3():
    n, = RI()
    a = RILST()
    trie = BinaryTrie(40)
    trie.add(0)
    ans = p = 0
    for v in a:
        p ^= v
        ans = max(ans, p)
        trie.add(p)
    p = 0
    for v in a[::-1]:
        p ^= v
        ans = max(ans, p, trie.find_max_xor(p))
    print(ans)


#    tle   ms
def solve2():
    n, = RI()
    a = RILST()
    trie = {}

    def insert(v):
        cur = trie
        for i in range(39, -1, -1):
            nxt = v >> i & 1
            if nxt not in cur:
                cur[nxt] = {}
            cur = cur[nxt]

    def find(v):
        cur = trie
        ret = 0
        for i in range(39, -1, -1):
            if v >> i & 1:
                if 0 in cur:
                    ret |= 1 << i
                    cur = cur[0]
                else:
                    cur = cur[1]
            else:
                if 1 in cur:
                    ret |= 1 << i
                    cur = cur[1]
                else:
                    cur = cur[0]
        return ret

    ans = p = 0
    insert(0)
    for v in a:
        p ^= v
        ans = max(ans, p)
        cur = trie
        for i in range(39, -1, -1):
            nxt = p >> i & 1
            if nxt not in cur:
                cur[nxt] = {}
            cur = cur[nxt]
    p = 0
    for v in a[::-1]:
        p ^= v
        cur = trie
        ret = 0
        for i in range(39, -1, -1):
            if p >> i & 1:
                if 0 in cur:
                    ret |= 1 << i
                    cur = cur[0]
                else:
                    cur = cur[1]
            else:
                if 1 in cur:
                    ret |= 1 << i
                    cur = cur[1]
                else:
                    cur = cur[0]
        ans = max(ans, p, ret)
    print(ans)


#    tle   ms
def solve1():
    n, = RI()
    a = RILST()
    trie = TrieXor([0], 40)
    ans = p = 0
    for v in a:
        p ^= v
        ans = max(ans, p)
        # if p > ans:
        #     ans = p
        trie.insert(p)
    p = 0
    for v in a[::-1]:
        p ^= v
        # if p > ans:
        #     ans = p
        # x = trie.find_max_xor_num(p)
        # if x > ans:
        #     ans = x
        ans = max(ans, p, trie.find_max_xor_num(p))
    print(ans)


if __name__ == '__main__':
    # n, = RI()
    # a = RILST()
    # trie = TrieXor([0], 40)
    # ans = p = 0
    # for v in a:
    #     p ^= v
    #     ans = max(ans, p)
    #     # if p > ans:
    #     #     ans = p
    #     trie.insert(p)
    # p = 0
    # for v in a[::-1]:
    #     p ^= v
    #     # if p > ans:
    #     #     ans = p
    #     # x = trie.find_max_xor_num(p)
    #     # if x > ans:
    #     #     ans = x
    #     ans = max(ans, p, trie.find_max_xor_num(p))
    # print(ans)
    # n, = RI()
    # a = RILST()
    # trie = {}
    #
    #
    # def insert(v):
    #     cur = trie
    #     for i in range(39, -1, -1):
    #         nxt = v >> i & 1
    #         if nxt not in cur:
    #             cur[nxt] = {}
    #         cur = cur[nxt]
    #
    #
    # def find(v):
    #     cur = trie
    #     ret = 0
    #     for i in range(39, -1, -1):
    #         if v >> i & 1:
    #             if 0 in cur:
    #                 ret |= 1 << i
    #                 cur = cur[0]
    #             else:
    #                 cur = cur[1]
    #         else:
    #             if 1 in cur:
    #                 ret |= 1 << i
    #                 cur = cur[1]
    #             else:
    #                 cur = cur[0]
    #     return ret
    #
    #
    # ans = p = 0
    # insert(0)
    # for v in a:
    #     p ^= v
    #     ans = max(ans, p)
    #     cur = trie
    #     for i in range(39, -1, -1):
    #         nxt = p >> i & 1
    #         if nxt not in cur:
    #             cur[nxt] = {}
    #         cur = cur[nxt]
    # p = 0
    # for v in a[::-1]:
    #     p ^= v
    #     cur = trie
    #     ret = 0
    #     for i in range(39, -1, -1):
    #         if p >> i & 1:
    #             if 0 in cur:
    #                 ret |= 1 << i
    #                 cur = cur[0]
    #             else:
    #                 cur = cur[1]
    #         else:
    #             if 1 in cur:
    #                 ret |= 1 << i
    #                 cur = cur[1]
    #             else:
    #                 cur = cur[0]
    #     ans = max(ans, p, ret)
    # print(ans)
    solve()
