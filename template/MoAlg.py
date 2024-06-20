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
