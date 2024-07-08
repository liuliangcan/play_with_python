"""迭代写法的zwk线段树，注意是0-indexed，注意query的时候是左闭右开[l,r)"""


class ZKW:
    # n = 1
    # size = 1
    # log = 2
    # d = [0]
    # op = None
    # e = 10 ** 15
    """自低向上非递归写法线段树，0_indexed
    tmx = ZKW(pre, max, -2 ** 61)
    """
    __slots__ = ('n', 'op', 'e', 'log', 'size', 'd')

    def __init__(self, V, OP, E):
        """
        V: 原数组
        OP: 操作:max,min,sum
        E: 每个元素默认值
        """
        self.n = len(V)
        self.op = OP
        self.e = E
        self.log = (self.n - 1).bit_length()
        self.size = 1 << self.log
        self.d = [E for i in range(2 * self.size)]
        for i in range(self.n):
            self.d[self.size + i] = V[i]
        for i in range(self.size - 1, 0, -1):
            self.update(i)

    def set(self, p, x):
        # assert 0 <= p and p < self.n
        update = self.update
        p += self.size
        self.d[p] = x
        for i in range(1, self.log + 1):
            update(p >> i)

    def get(self, p):
        # assert 0 <= p and p < self.n
        return self.d[p + self.size]

    def query(self, l, r):  # [l,r)左闭右开
        # assert 0 <= l and l <= r and r <= self.n
        sml, smr, op, d = self.e, self.e, self.op, self.d

        l += self.size
        r += self.size

        while l < r:
            if l & 1:
                sml = op(sml, d[l])
                l += 1
            if r & 1:
                smr = op(d[r - 1], smr)
                r -= 1
            l >>= 1
            r >>= 1
        return self.op(sml, smr)

    def all_query(self):
        return self.d[1]

    def max_right(self, l, f):
        """返回l右侧query(l,p)第一个不满足f的位置p"""
        # assert 0 <= l and l < self.n
        # assert f(self.e)
        if l == self.n:
            return self.n
        l += self.size

        sm, op, d, size = self.e, self.op, self.d, self.size
        while True:
            while l % 2 == 0:
                l >>= 1
            if not (f(op(sm, d[l]))):
                while l < size:
                    l = 2 * l
                    if f(op(sm, d[l])):
                        sm = op(sm, d[l])
                        l += 1
                return l - size
            sm = op(sm, d[l])
            l += 1
            if (l & -l) == l:
                break
        return self.n

    def min_left(self, r, f):
        """返回r左侧query(p,r)连续满足f的最远位置的位置,注意这个r要按开区间写，即+1"""
        # assert 0 < r and r <= self.n
        # assert f(self.e)
        if r == 0:
            return 0
        r += self.size
        sm, op, d, size = self.e, self.op, self.d, self.size

        while True:
            r -= 1
            while r > 1 and (r % 2):
                r >>= 1
            if not (f(op(d[r], sm))):
                while r < size:
                    r = (2 * r + 1)
                    if f(op(d[r], sm)):
                        sm = op(d[r], sm)
                        r -= 1
                return r + 1 - size
            sm = op(d[r], sm)
            if (r & -r) == r:
                break
        return 0

    def update(self, k):
        self.d[k] = self.op(self.d[k << 1], self.d[k << 1 | 1])

    def __str__(self):
        return str([self.get(i) for i in range(self.n)])


"""
区间最大子段，带修改：P4513 小白逛公园 https://www.luogu.com.cn/problem/P4513  注意这题这么写会MLE，还是需要写4个数组去做，可以过
    def op(x, y):
        x1, y1, z1, k1 = x  # 和，最大子段和，最大前缀和，最大后缀和, 答案是ret[1]
        x2, y2, z2, k2 = y
        return x1 + x2, max(y1, y2, k1 + z2), max(z1, x1 + z2), max(k2, k1 + x2)
    tree = ZKW([(v, v, v, v) for v in a], op, (-inf, -inf, -inf, -inf))
    
区间打家劫舍 3165. 不包含相邻元素的子序列的最大和: https://leetcode.cn/problems/maximum-sum-of-subsequence-with-non-adjacent-elements/description/
    def op(x,y):
        f11,f10,f01,f00 = x 
        g11,g10,g01,g00 = y 
        return max(f11+g01,f10+g11), max(f10+g10,f11+g00),max(f00+g11,f01+g01),max(f00+g10,f01+g00)
    zkw = ZKW([(v,0,0,0) for v in nums],op,(0,0,0,0)
    
区间与：zkw = ZKW(nums,and_,-1)   # -1就是全1，相当于(1<<n)-1  https://leetcode.cn/problems/find-subarray-with-bitwise-and-closest-to-k/

区间rk2的计数：在线带修询问区间内第二大的数的计数，用字典存卡常；  https://atcoder.jp/contests/abc343/tasks/abc343_f
    这题也可以存前两个的下标,改一下加号就行: https://codeforces.com/problemset/problem/1927/D
    def f(a, b, c, d):
        if a == c:
            return a, b + d
        elif a < c:
            return c, d
        else:
            return a, b

    def op(x, y):
        if x > y:
            x, y = y, x
        if x[0] == y[0]:
            a, b = x[0], x[1] + y[1]
            c, d = f(x[2], x[3], y[2], y[3])
        else:
            a, b = y[0], y[1]
            c, d = f(x[0], x[1], y[2], y[3])
        return a, b, c, d

    zkw = ZKW([(v, 1, 0, 0) for v in a], op, (0, 0, 0, 0))
"""