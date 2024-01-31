"""马拉车算法：利用dp加速中心扩展法
用途：
1. O(n)找到每个字符为中心的最长（任意长度）回文串；
2. O(n)预处理后，O(1)判断一个区间是否是回文。
简介：
1. 通过插入扩展字符，使每个回文串长度都是奇数（保证有中心）
2. 记录dp[i]和当前最右回文串，若当前i<=R,则可以直接取对称位置的dp[i],加速扩展
复杂度：初始化O(n)
1. 由于用dp对称位置加速，我们发现当dp[i]的右端点<R时，镜像位置左端点一定>L,那么当前位置无需继续扩展（否则对称位置也能扩展）。
2. 因此每个位置只会作为右边界被扩展成功一次，每个中心点只会扩展失败一次。因此总体是O(n)
一篇很清晰的讲解：https://leetcode.cn/problems/palindrome-partitioning-ii/solutions/369625/manacher-o1pan-duan-ren-yi-zi-chuan-shi-fou-hui-we/
"""


class Manacher:
    def __init__(self, s):
        """马拉车用dp加速中心扩展法"""
        self.s = s
        s1 = ['#']  # 增加扩展字符
        for c in s:
            s1.extend([c, '#'])
        n = len(s1)
        f = self.f = [1] * n  # 扩展串上以i为中心的最长回文串长度
        l, r = 0, -1
        for i in range(n):
            if i <= r:  # 如果i包含在已知回文串里，那么可以用对称点信息加速，但不能超过边界
                f[i] = min((r - i) * 2 + 1, f[r + l - i])
            l1, r1 = i - f[i] // 2 - 1, i + f[i] // 2 + 1
            while 0 <= l1 and r1 < n and s1[l1] == s1[r1]:  # 继续尝试扩展
                l1, r1 = l1 - 1, r1 + 1
            f[i] = r1 - l1 - 1
            if r1 > r:  # 更新r，这里存疑，如果变短也要更新吗？随便测了一个r1>r+1也能过。
                l, r = l1 + 1, r1 - 1

    def get_longest_palindrome(self):  # O(n)
        return max(self.f) // 2  # 原串上的最长回文串，去掉扩展符

    def get_all_pal_of_len(self, d):  # 获取所有长度为d的回文串起止位置[闭区间]O(n)
        d2 = d * 2 + 1  # 转化成在扩展串上的长度
        for i, v in enumerate(self.f):
            if v >= d2:
                yield (i - d) >> 1, (i + d - 1) >> 1  # 注意右边要-1

    def is_palindrome(self, l, r):
        return self.f[l + r + 1] >= (r * 2 - l * 2 + 1)  # 原串上[l,r]是否是回文;在扩展串上映射的下标是l*2+1和r*2+1;f[mid]>=r1-l1+1即可


class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        # f = [[0]*n for _ in range(n)]
        # for l in range(n-1, -1, -1):
        #     f[l][l] = 1
        #     if l:
        #         f[l][l-1] = 1
        #     for r in range(l+1, n):
        #         if s[l] == s[r] and f[l+1][r-1]:
        #             f[l][r] = 1
        mnc = Manacher(s)
        dp = [0] * (n + 1)
        for i in range(n):
            dp[i + 1] = dp[i] + 1
            for j in range(i - 1, -1, -1):
                if mnc.is_palindrome(j, i):
                    dp[i + 1] = min(dp[i + 1], dp[j] + 1)

        return dp[-1] - 1
