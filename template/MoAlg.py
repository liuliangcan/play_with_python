"""莫队
离线，用nsqrt(n)的时间处理区间q个询问(这里认为nq同阶，实际会有区别)
本质是分块，把所有询问按照 (l所在块序号，r) 进行排序。然后用全局L,R在序列上按照询问顺序进行移动回答问题。
    -- 显然，要求L,R移动时，对答案的贡献可以O(1)贡献/回退出来。
步骤：
    - 把询问按照(l所在块序号，r)排序。
    - 定义全局L,R =0,-1 代表当前区间，全局ans以及其他信息。
    - 按照顺序依次处理询问:
            while L > l: L -= 1; add_left(L);
            while R < r: R += 1; add_right(R)
            while L < l: remove_left(L); L += 1;
            while R > r:  remove_right(R); R -= 1;
            res[i] = get()
复杂度（重点）：分别讨论L,R的移动次数
    - R: 在某个块(指按L标号分的相邻询问)内，R是从0~n的。块间移动也是n，一共sqrt(n)个块。因此是n*sqrt(n)
    - L: 在某个块内，L每次移动是sqrt(n),最多q次，则是q*sqrt(n)。块间移动最差sqrt(n),一共sqrt(n)个，因此是n;总计是n+n*sqrt(n)
    - 因此总共是n*sqrt(n)
    -----
    - 详细计算：
    - 设块大小是b,那么R移动次数是 n*n/b,L是b*q+n,总共是n*n/b+b*q。 粗略的讲，b=n/sqrt(q)时最小。
优化
    - 对询问r进行奇偶排序，这样移动到下个块时，不用重复从n移到1重新开始，而是从大的开始顺路。这样可以减一半。整体效率提高30%。
    - 对询问进行状压，比对元组操作快很多。由于莫队题目的n和q通常是1e5级别(<1e6),可以用60位把这三个数都压起来。
    - 剪枝（按理说应该没用）lc3762. 使数组元素相等的最小操作次数。 这题有的询问是非法的，可以O(1)剔除，那这种情况下，只需要add其它询问。
        这时，self.query不要初始化成q了，直接append
        同时，res不要在solve里创建，传进去，不影响已经算过的剪枝的询问。
        这题剪不剪枝从TLE变成2.8s飞快。但如果题目数据有那种[1]*n,剪枝无效的话，其实没有意义
        这题还要用对顶堆，所以总复杂度是nsqrtnlogn
例题
    - 模板 G - Range Pairing Query https://atcoder.jp/contests/ABC242/tasks/abc242_g
"""


class Mo:
    def __init__(self, N, Q):
        self.q = Q
        self.n = N
        self.query = [0] * Q
        self.data = [0] * Q
        self.bsize_ = int(max(1, n / max(1, (q * 2 / 3) ** 0.5)))
        # W = max(1, int(N / sqrt(Q)))

    def add_query(self, l, r, i):
        self.data[i] = l << 20 | r
        self.query[i] = ((l // self.bsize_) << 40) + ((-r if (l // self.bsize_) & 1 else r) << 20) + i

    def solve(self):
        data = self.data
        self.query.sort()
        L, R = 0, -1
        res = [0] * self.q
        mask = (1 << 20) - 1
        for lri in self.query:
            i = lri & mask
            lr = data[i]
            l, r = lr >> 20, lr & mask
            while L > l: L -= 1; add_left(L);
            while R < r: R += 1; add_right(R)
            while L < l: remove_left(L); L += 1;
            while R > r:  remove_right(R); R -= 1;
            res[i] = get()
        return res


def add_left(x):
    global cnt
    cnt += C[a[x]]
    C[a[x]] ^= 1


def add_right(x):
    global cnt
    cnt += C[a[x]]
    C[a[x]] ^= 1


def remove_left(x):
    global cnt
    C[a[x]] ^= 1
    cnt -= C[a[x]]


def remove_right(x):
    global cnt
    C[a[x]] ^= 1
    cnt -= C[a[x]]


def get():
    return cnt


n, = RI()
a = RILST()
q, = RI()

C = [0] * (n + 1)
cnt = 0
mo = Mo(n, q)
for i in range(q):
    l, r = RI()
    mo.add_query(l - 1, r - 1, i)
res = mo.solve()
print('\n'.join(map(str, res)))


################  以下是lc3762. 使数组元素相等的最小操作次数  的代码，算是优化剪枝的案例，但极端数据其实无效；如果题目一定可以剪枝，那就有效

class DualHeap:
    """对顶堆，实时计算当前集合前k小的元素和(如果k设0,则保持平衡，0<=small-large<=1)。每个操作均摊时间复杂度O(lgn)，总体O(nlgn)。682ms"""

    def __init__(self, k=0):
        self.k = k  # 如果k=0，表示保持两个堆一样大(0<=small-large<=1),此时-small[0]就是中位数
        self.small = []  # 大顶堆存较小的k个数，注意py默认小顶堆，因此需要取反
        self.large = []  # 小顶堆存较大的剩余数
        self.delay_rm = defaultdict(int)  # 延时删除标记
        self.sum_kth = 0  # 前k小数字的和
        self.small_size = 0
        self.large_size = 0

    def prune(self, h):
        """修剪h，使h堆顶的已标记删除元素全部弹出"""
        delay_rm = self.delay_rm
        p = -1 if h is self.small else 1
        while h:
            v = h[0] * p
            if v in delay_rm:
                delay_rm[v] -= 1
                if not delay_rm[v]:
                    del delay_rm[v]
                heappop(h)
            else:
                break

    def make_balance(self):
        """调整small和large的大小，使small中达到k个（或清空large）"""
        k = self.k or (self.small_size + self.large_size + 1) // 2  # 如果self.k是0，表示前后要balance
        if self.small_size > k:
            heappush(self.large, -self.small[0])
            self.sum_kth += heappop(self.small)  # 其实是-=负数
            self.large_size += 1
            self.small_size -= 1
            self.prune(self.small)
        elif self.small_size < k and self.large:
            heappush(self.small, -self.large[0])
            self.sum_kth += heappop(self.large)
            self.small_size += 1
            self.large_size -= 1
            self.prune(self.large)

    def add(self, v):
        """添加值v，判断需要加到哪个堆"""
        small = self.small
        if not small or v <= -small[0]:
            heappush(small, -v)
            self.sum_kth += v
            self.small_size += 1
        else:
            heappush(self.large, v)
            self.large_size += 1
        self.make_balance()

    def remove(self, v):
        """移除v，延时删除，但可以实时判断是否贡献了前k和"""
        small, large = self.small, self.large
        self.delay_rm[v] += 1
        if large and v >= large[0]:
            self.large_size -= 1
            if v == large[0]:
                self.prune(large)
        else:
            self.small_size -= 1
            self.sum_kth -= v
            if v == -small[0]:
                self.prune(small)
        self.make_balance()


class Solution:
    def minOperations(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)
        a = [v % k for v in nums]

        class Mo:
            def __init__(self, N, Q):
                self.q = Q
                self.n = N
                self.query = []
                self.data = [0] * Q
                self.bsize_ = int(max(1, n / max(1, (Q * 2 / 3) ** 0.5)))
                # W = max(1, int(N / sqrt(Q)))

            def add_query(self, l, r, i):
                self.data[i] = l << 20 | r
                self.query.append(((l // self.bsize_) << 40) + ((-r if (l // self.bsize_) & 1 else r) << 20) + i)

            def solve(self, res):
                data = self.data
                self.query.sort()
                L, R = 0, -1
                # res = [0] * self.q
                mask = (1 << 20) - 1
                for lri in self.query:
                    i = lri & mask
                    lr = data[i]
                    l, r = lr >> 20, lr & mask
                    while L > l: L -= 1; add_left(L, R);
                    while R < r: R += 1; add_right(L, R)
                    while L < l: remove_left(L, R); L += 1;
                    while R > r:  remove_right(L, R); R -= 1;
                    res[i] = get()
                return res

        def add_left(x, R):
            nonlocal s, diff
            v = nums[x]
            s += v
            dh.add(v)
            if x < R:
                diff += a[x] != a[x + 1]

        def add_right(L, x):
            nonlocal s, diff
            v = nums[x]
            s += v
            dh.add(v)
            if L < x:
                diff += a[x] != a[x - 1]

        def remove_left(x, R):
            nonlocal s, diff
            v = nums[x]
            s -= v
            dh.remove(v)
            if x < R:
                diff -= a[x] != a[x + 1]

        def remove_right(L, x):
            nonlocal s, diff
            v = nums[x]
            s -= v
            dh.remove(v)
            if L < x:
                diff -= a[x] != a[x - 1]

        def get():
            if diff: return -1
            x, y = dh.small_size, dh.large_size
            if x + y == 1: return 0
            mid = -dh.small[0]
            left = dh.sum_kth
            return (mid * x - left + s - left - mid * y) // k

        diff = []
        for x, y in pairwise(nums):
            diff.append(int(y % k != x % k))
        dpre = [0] + list(accumulate(diff))

        s = 0
        diff = 0
        dh = DualHeap()
        q = len(queries)
        mo = Mo(n, q)
        ans = [0] * q
        for i, (l, r) in enumerate(queries):
            if l == r:
                ans[i] = 0
                continue
            if dpre[r] - dpre[l]:
                ans[i] = -1
                continue
            mo.add_query(l, r, i)
        res = mo.solve(ans)
        return res
