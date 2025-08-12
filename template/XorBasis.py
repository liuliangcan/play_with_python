"""异或线性基，时间复杂度O(nlogU)
求一组数的异或线性基，可以：
1. 求一组数的任意子集的最大/最小/第k大/第k小异或和
2. 判断一个数能否表示成某数集的异或和
3. 求一个数表示成某数集子集异或和的方案数
4. 求一个数在某数集子集异或和中的排名
例题：https://codeforces.com/gym/105974 cf xbasis专项
1. 3630. 划分数组得到最大异或运算和与运算之和
https://leetcode.cn/problems/partition-array-for-maximum-xor-and-and/description/
2.https://codeforces.com/problemset/problem/1101/G ,任取若干子段，异或和要互异，求前缀和的线性基数量即可，但是由于前缀和可以被原数组表出，也可以直接求原数组的线性基
3.https://codeforces.com/problemset/problem/959/F 问某个数可以被用多少种方式表出，增量构造线性基
4. https://codeforces.com/gym/105974/problem/A A. Distinct Xor Subsequences一组数异或能表出的数字数量，其实就是pow(2,len(b))
5. https://codeforces.com/gym/105974/problem/B B. Distinct Xor Subsequence Queries 第k小异或和，可选空，b排序，k按位取即可
6. https://codeforces.com/gym/105974/problem/C C. Distinct Xor Subsequence Queries Ⅱ 同CF959F，增量构造，pow(2,n-len(b))
7. https://codeforces.com/gym/105974/problem/D D. Range Xor Subsequence Query  前缀线性基,通过每个基记录最右位置,这样直接取base[r],判断位置>=l的即可,同https://atcoder.jp/contests/abc223/tasks/abc223_h
8. https://codeforces.com/gym/105974/problem/E E. Constructive Xor 表出一个数值的具体方案,需要用mask把每位的状态都记下来

前缀线性基:
对数组a的每个位置i记录1~i的线性基副本,并且每个基多维护一个pos[j],代表这个基出现的最右位置,这样问[l,r]的线性基时,只需要筛选pos>=l的即可.
表出数字的具体方案:对每个基额外用个bitset记录它用了哪些数字异或到一起的,然后表的时候都异或起来即可

其他:
1. 推荐用quick那个模板,即基于x=min(x,x^v)的方法,代码短,好写,跑得快;但有的题还是得用贪心法,比如前缀线性基/构造具体方案
2. 高斯消元除了求kth几乎用不到,而且可以先用另外两个方法求线性基,需要求kth时再消,因为最多消len(b)次
"""
from typing import List




class XorBasisGauss:
    """高斯消元构造线性基，拥有比贪心法更好的性质;从高位找对应位有1的数，换到数组a的前边来，最后a[:cnt]就是基"""

    def __init__(self, n, a):
        cnt = 0
        self.a = a
        sz = len(a)
        for i in range(n - 1, -1, -1):
            for j in range(cnt, sz):
                if a[j] >> i & 1:
                    a[j], a[cnt] = a[cnt], a[j]
                    break
            else:
                continue
            for j in range(sz):
                if a[j] >> i & 1 and j != cnt:
                    a[j] ^= a[cnt]
            if cnt == sz: break
        self.cnt = cnt

    def can_present(self, v):
        for i in range(self.cnt):
            v = min(v, v*self.a[i])
        return v == 0

    def find_max_xor(self):
        res = 0
        for i in range(self.cnt):
            res ^= self.a[i]
        return res


class XorBasisGreedy:
    """贪心法构造线性基，基于每个高位计算；1.每个基的最高位不同。2.基中没有异或为0的子集"""

    def __init__(self, n):
        self.b = [0] * n
        self.gauss = False

    def insert(self, v):
        while v:
            i = v.bit_length() - 1
            if self.b[i] == 0:
                self.b[i] = v
                self.gauss = False
                break
            v ^= self.b[i]

    def can_present(self, v):
        while v:
            i = v.bit_length() - 1
            if self.b[i] == 0:
                return False
            v ^= self.b[i]
        return v == 0

    def find_max_xor(self):
        res = 0
        b = self.b
        for i in range(len(b) - 1, -1, -1):
            if res ^ b[i] > res:
                res ^= b[i]
        return res

    def kth(self, k):  # 第k小,k从1数
        if not self.gauss:  # 需要消元,最多做len(b)次
            self.gauss = True
            for i, x in enumerate(self.b):
                if x:
                    for j in range(i + 1, len(self.b)):
                        if self.b[j] >> i & 1:
                            self.b[j] ^= x
        b = [v for v in self.b if v]
        if 1 << len(b) < k: return -1
        k -= 1
        ans = 0
        for i, x in enumerate(b):
            if k >> i & 1:
                ans ^= x
        return ans


class XorBasisQuick:
    """贪心法构造线性基，基于每个高位计算"""

    def __init__(self):
        self.b = []
        self.gauss = 0  # 前gauss个已经做过高斯消元

    def insert(self, x):
        for v in self.b:
            if x ^ v < x:
                x ^= v
        if x:
            self.b.append(x)

    def can_present(self, x):
        for v in self.b:
            x = min(x, x ^ v)
        return x == 0

    def find_max_xor(self):  # 这个很慢
        if self.gauss < len(self.b):
            self.do_gauss()
        res = 0
        for v in self.b:
            res ^= v
        return res

    def do_gauss(self):
        b = self.b
        n = len(b)
        for i in range(self.gauss, n):
            for j in range(i):
                # b[j] = min(b[j], b[j] ^ b[i])
                if b[j] ^ b[i] < b[j]:
                    b[j] ^=b[i]
        b.sort()
        self.gauss = n

    def kth(self, k):
        b = self.b
        if 1 << len(b) < k:
            return -1
        if self.gauss < len(b):
            self.do_gauss()
        k -= 1
        ans = 0
        for i, v in enumerate(b):
            if k >> i & 1:
                ans ^= v
        return ans
class Solution:
    def maximizeXorAndXor(self, nums: List[int]) -> int:
        n = len(nums)
        m = 1 << n
        ans = 0
        xors = [0]*m
        ands = [-1]*m
        ors = [0]*m
        for i, v in enumerate(nums):
            u = 1 << i
            for j in range(u):
                xors[j|u] = xors[j]^v
                ands[j|u] = ands[j]&v
                ors[j|u] = ors[j]|v
        ands[0] = 0
        u = max(nums).bit_length()
        for i in range(m):
            if ands[i] + ors[(m-1)^i]*2 - xors[(m-1)^i] <= ans:continue
            base = XorBasisGreedy(u)
            xor = ~xors[(m-1)^i]
            for j in range(n):
                if not i >> j & 1:
                    base.insert(nums[j]&xor)
            p = base.find_max_xor()

            ans = max(ans, ands[i]+p*2 + ~xor)
        return ans


print(Solution().maximizeXorAndXor([165,23,102]))




# 前缀线性基模板,贪心法
class PrefixXorBasis:
    def __init__(self, a, n):
        # self.n = n
        self.bs = bs = []
        self.ps = ps = []
        b = [0] * n
        p = [-1] * n
        for i, x in enumerate(a):
            while x:
                j = x.bit_length() - 1
                if b[j] == 0:
                    b[j] = x
                    p[j] = i
                    break
                if p[j] < i:
                    p[j], i = i, p[j]
                    x, b[j] = b[j], x
                x ^= b[j]
            bs.append(b[:])
            ps.append(p[:])

    def get_basis_less(self, l, r):  # 获取[l,r]的线性基,0-based,没有0
        return [x for x, y in zip(self.bs[r], self.ps[r]) if y >= l]

    def get_basis(self, l, r):  # 获取[l,r]的线性基,0-based
        return [x if y >= l else 0 for x, y in zip(self.bs[r], self.ps[r])]

    def can_present(self, l, r, x):  # [l,r]里能否表出x,0-based
        p = self.ps[r]
        if x == 0:
            return len([1 for i in p if i >= l]) < r - l + 1
        else:
            b = self.bs[r]
            while x:
                i = x.bit_length() - 1
                if b[i] == 0 or p[i] < l:
                    return False
                x ^= b[i]
            return True
