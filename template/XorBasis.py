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
"""
from typing import List



class XorBasisGreedy:
    """贪心法构造线性基，基于每个高位计算；1.每个基的最高位不同。2.基中没有异或为0的子集"""

    def __init__(self, n):
        self.b = [0] * n

    def insert(self, v):
        while v:
            i = v.bit_length() - 1
            if self.b[i] == 0:
                self.b[i] = v
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
class XorBasisQuick:
    """贪心法构造线性基，基于每个高位计算"""
    def __init__(self):
        self.b = []

    def insert(self, v):
        for x in self.b:
            if v ^ x < v:
                v ^= x
        if v:
            self.b.append(v)
    def can_present(self,v):
        for x in self.b:
            v = min(v,x^v)
        return v == 0
    def find_max_xor(self):  # 这个很慢
        res = 0
        for v in sorted(self.b, reverse=True):
            if res ^ v > res:
                res ^= v
        return res


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