"""回滚莫队
其实是比普通莫队更普适,且好写的算法;但是无法应用奇偶排序的优化,所以会慢一些
我们知道<普通莫队>是按左端点分组,组内右端点排序;这样分组处理,右端点就可以每次都一路同方向,是n,组内左端点在blocksize范围抖动;因此左右端点分别各移动最多qlogn和nlogn次
回滚莫队去掉了删除操作,只用添加:先确保l和r在不同组(r-l+1<=bsize的暴力计算),对每一组,R一定从lb+1组的左端点开始\直到n,L对每个询问都从lb组的最后开始\问完回退,这样L一定是增加的,左端点就不需要抖动了

步骤：
    - 把询问按照(l所在块序号，r)排序。
    - 分组处理:
        - 初始化R=下一个组的第一个位置,记作R'
        - 贡献右端点while R<=r:add_right(R++)
        - 记录当前[R',r]的状态 tmp=get()
        - 贡献左端点for i in range(l,R'):add_left(i);注意这里i顺序可能随意,也可能有的题目要求顺序.
        - 贡献[l,r]的答案
        - 回退状态到tmp,即[R',r],下次计算重新贡献左端点. (注意,如果状态不止单纯数字,比如cnt,也要回退)

复杂度（重点）：分别讨论L,R的移动次数
    - R: 在某个块(指按L标号分的相邻询问)内，R是从0~n的。块间移动也是n，一共sqrt(n)个块。因此是n*sqrt(n)
    - L: 在某个块内，L每次移动是sqrt(n),最多q次，则是q*sqrt(n)。块间移动最差sqrt(n),一共sqrt(n)个，因此是n;总计是n+q*sqrt(n)
    - 因此总共是n*sqrt(n) + qsqrt(n)
    -----
    - 详细计算：
    - 设块大小是b,那么R移动次数是 n*n/b,L是b*q+n,总共是n*n/b+b*q。 粗略的讲，b=n/sqrt(q)时最小。
优化
    - 对询问进行状压，比对元组操作快很多。由于莫队题目的n和q通常是1e5级别(<1e6),可以用60位把这三个数都压起来。

例题
    - 模板 3636. 查询超过阈值频率最高元素 https://leetcode.cn/problems/threshold-majority-queries/description/
"""
from collections import defaultdict


class MoRollBackAdd:
    def __init__(self, N, Q):
        self.q = Q
        self.n = N
        self.query = []
        self.data = [0] * Q
        self.bsize_ = int(max(1, n / max(1, (q * 2 / 3) ** 0.5)))
        # W = max(1, int(N / sqrt(Q)))
        self.res = [0] * q

    def add_query(self, l, r, i):
        if r - l + 1 <= self.bsize_:
            reset()
            for i in range(l, r + 1):
                add_right(i)
            self.res = get()
            return
        self.data[i] = l
        self.query.append(((l // self.bsize_) << 40) + (r << 20) + i)

    def solve(self):

        data = self.data
        query = self.query
        bsize = self.bsize_
        query.sort()
        mask = (1 << 20) - 1
        R = 0
        for idx, lri in enumerate(self.query):
            lb = lri >> 40
            r = (lri >> 20) & mask
            i = lri & mask
            l = data[i]
            if idx == 0 or lb != (query[idx - 1] >> 40):
                R = (lb + 1) * bsize
                reset()
            while R <= r:
                add_right(R)
                R += 1
            tmp()  # 记录临时状态
            for j in range((lb + 1) * bsize - 1, l - 1, -1):
                add_left(j)
            self.res[i] = get()
            rollback(l, (lb + 1) * bsize - 1)

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


def get():
    return cnt


def reset():
    global C, cnt
    C = [0] * (n + 1)
    cnt = 0


def tmp():
    global tmp_cnt
    tmp_cnt = cnt


def rollback(l, r_):
    global cnt
    cnt = tmp_cnt
    for i in range(l, r_ + 1):
        remove_left(i)


n, = RI()
a = RILST()
q, = RI()

C = [0] * (n + 1)
cnt = 0
tmp_cnt = 0
mo = Mo(n, q)
for i in range(q):
    l, r = RI()
    mo.add_query(l - 1, r - 1, i)
res = mo.solve()
print('\n'.join(map(str, res)))
