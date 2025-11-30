"""SOSDP, 子集和 DP（Sum Over Subsets DP，SOS DP），国内算法竞赛圈一般叫高维前缀和
可以在O(n+UlogU)的时间里计算出每个状态的子集的数字数量，
通过这个可以再扩展其它组合计算


DP:
定义: f[i][S]表示 前i位都保留，是S的子集的元素个数
转移：
    a. 如果S第i位是0，只能不选，问题变成S前i-1位都保留，即
        f[i][S] = f[i-1][S]
    b. 如果S第i位是1，讨论选或不选
        选，问题变成S前i-1位都保留，即
        f[i][S] = f[i-1][S]
        不选，问题变成S^(1<<i)前i-1位都保留，即
        f[i][S] = f[i-1][S^(1<<i)]
    显然这里有点像背包，可以滚动优化，判断i位是1的话再加即可
初始：f[-1][S] = cnt[S]
答案：f[W-1][S] 代表整个数组，S子集的数字个数

实现：
1. 先压位，确定位长W，那么U=1<<W,注意后续都是基于U和W进行枚举了,所以复杂度是UlogU而不是nlogU
2. 统计cnt[v]
3. f=cnt.copy() 然后对f进行SOSDP


注意:
1. for i in range(w) 一定要写在外层，才能不重不漏
2. 如果没压位，最后处理贡献答案时，一定要注意判断是否是T的子集，才贡献
优化：
1. 最明显的是压缩位，仅留存输入中有1的位。即去掉仅含0的位，这样可以优化很多，但是对极限数据没用
2. 不压位的话，可以枚举j时，每次都|=bit, 这样可以快速跳到第i位是1的数字
3. SOS时，bit提前算出来，可以服用n次；SOS时，如果没压位，那么如果bit不是t的子集，可以直接跳过
4. 后边容斥的时候，记得是i和t的位差如果是偶数则+，奇数则-。记得，得是t的子集才算（这里要么用子集枚举，要么压位；显然压位更方便）


例题：
1. lc 3757. 有效子序列的数量 https://leetcode.cn/problems/number-of-effective-subsequences/  典题，SOSDP+容斥
2. lc 3670. 没有公共位的整数最大乘积 https://leetcode.cn/problems/maximum-product-of-two-integers-with-no-common-bits/ 需要计算每个状态子集的最大值，而不是计数
3. lc 2044. 统计按位或能得到最大值的子集数目 https://leetcode.cn/problems/count-number-of-maximum-bitwise-or-subsets/ SOSDP+容斥

## 以下是 lc 3757. 有效子序列的数量
MOD = 10 ** 9 + 7
N = 10 ** 5
pw2 = [1] * (N + 1)
for i in range(1, N + 1):
    pw2[i] = pw2[i - 1] * 2 % MOD


class Solution:
    def countEffective(self, nums: List[int]) -> int:
        n = len(nums)
        t = reduce(ior, nums)
        W = t.bit_count()
        U = 1 << W
        bits = []  # 压位
        for i in range(t.bit_length()):
            if t >> i & 1:
                bits.append(i)
        f = [0] * U
        for v in nums:
            s = 0
            for j in range(W):
                if v >> bits[j] & 1:
                    s |= 1 << j
            f[s] += 1
        for i in range(W):
            mask = 1 << i
            for v in range(U):
                if v & mask:
                    f[v] += f[v ^ mask]
        t = U - 1
        ans = pw2[n]
        for s in range(U):
            if (s ^ t).bit_count() & 1:
                ans += pw2[f[s]]
            else:
                ans -= pw2[f[s]]

        return ans % MOD

##  lc 3670. 没有公共位的整数最大乘积
max=lambda x,y:x if x>y else y
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        t = reduce(or_, nums)
        W = t.bit_count()
        U = 1 << W
        bits = []
        for i in range(t.bit_length()):
            if t >> i & 1:
                bits.append(i)
        f = [0]*U

        for v in nums:
            s = 0
            for j in range(W):
                if v >> bits[j] & 1:
                    s |= 1<<j
            f[s] = v
        for i in range(W):
            bit = 1 << i
            for v in range(U):
                if v & bit:
                    f[v] = max(f[v], f[v^bit])
        ans = 0
        U -= 1
        for v in nums:
            s = 0
            for j in range(W):
                if v >> bits[j] & 1:
                    s |= 1<<j
            ans = max(ans, f[s]*f[U^s])
        return ans

## 不压位写法，较慢
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        t = reduce(or_, nums)
        W = t.bit_length()
        U = 1 << W

        f = [0] * U

        for v in nums:
            f[v] = v
        for i in range(W):
            bit = 1 << i
            for v in range(U):
                if v & bit:
                    f[v] = max(f[v], f[v ^ bit])
        ans = 0
        U -= 1
        for v in nums:
            ans = max(ans, f[v] * f[U ^ v])
        return ans
# 不压位，但是快速跳到bit位1的数，省去没用的循环
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        w = max(nums).bit_length()
        u = 1 << w
        f = [0] * u
        for x in nums:
            f[x] = x

        for i in range(w):
            bit = 1 << i  # 避免在循环中反复计算 1 << i
            s = 0
            while s < u:
                s |= bit  # 快速跳到第 i 位是 1 的 s
                f[s] = max(f[s], f[s ^ bit])
                s += 1

        return max(x * f[(u - 1) ^ x] for x in nums)
