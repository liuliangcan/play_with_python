"""最大子段和
基础的最大子段和：Kadane或者用前缀和+哈希表
lc644(会员题), 求最大子段平均值(长度不少于k)，
    - 类似分数规划，二分，https://oi-wiki.org/misc/frac-programming/
    - 二分答案，check时，把所有v-avg,那么一个子段和超过0，则这段的平均值超过avg.
    - 问题转化成求长度超过k的最大字段和，这可以前缀和+双指针解决
求长度不超过k，或超过k的的最大字段和，两种方法。 https://codeforces.com/problemset/problem/1796/D
    - 长度超过k的最大子段和，这可以前缀和+双指针解决
    - 长度不超过k的最大子段和，用前缀和+单调队列
区间最大子段和,由分治方法改造：https://www.luogu.com.cn/problem/P4513
    - 线段树
"""


def kadane(a):
    ans, s = a[0], 0
    for v in a:
        s = max(0, s) + v
        ans = max(ans, s)
    return ans


def get_max_sub_array_under_k(a, k):
    """长度<=k的最大子段和，不含空"""
    if k == 0:  # 长度不超过0那只好是空，看情况非法值修改成0或其他
        return -inf
    ans = -inf
    pre = [0] + list(accumulate(a))
    q = deque([0])  # 单调递增队列
    for i, v in enumerate(pre):
        while q[0] + k < i:
            q.popleft()  # k以外，出窗

        ans = max(ans, v - pre[q[0]])
        while q and pre[q[-1]] >= pre[i]:
            q.pop()  # 留小的
        q.append(i)
    return ans


def get_max_sub_array_over_k(a, k):
    """长度>=k的最大子段和,双指针+前缀和;注意k=0的情况，那就是没限制"""
    if k == 0: return kadane(a)

    ans = -inf
    pre = pre2 = mn = 0

    for i, v in enumerate(a):
        pre += v
        if i >= k - 1:
            ans = max(ans, pre - mn)
            pre2 += a[i - k + 1]
            mn = min(mn, pre2)

    return ans



def solve1():
    """最大子段平均数，分数规划，二分答案转化成不短于k的最大子段和问题"""
    n, f = map(int, input().split())
    a = []
    for _ in range(n):
        a.append(int(input()))

    def ok(x):
        s = p = mp = 0
        for i in range(f):
            s += a[i] - x
        if s >= 0:
            return False
        for i in range(f, n):
            s += a[i] - x
            p += a[i - f] - x
            mp = min(mp, p)
            if s - mp >= 0:
                return False
        return True

    l, r = sum(a[:f]) / f, sum(a)

    if l > r:
        l, r = r, l

    for _ in range(60):
        mid = (l + r) / 2
        if ok(mid):
            r = mid
        else:
            l = mid

    print(int(l * 1000))


"""  区间最大子段和
(v, v, v, v)
x,y,z,k = x1+x2, max(y1,y2,k1+z2),max(z1, x1+z2), max(k2,k1+x2)
"""

def op(x, y):
    x1, y1, z1, k1 = x  # 和，最大子段和，最大前缀和，最大后缀和, 答案是ret[1]
    x2, y2, z2, k2 = y
    return x1 + x2, max(y1, y2, k1 + z2), max(z1, x1 + z2), max(k2, k1 + x2)

tree = ZKW([(v, v, v, v) for v in a], op, (-inf, -inf, -inf, -inf))