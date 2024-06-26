"""马拉车算法：利用dp加速中心扩展法
用途：
1. O(n)找到每个字符为中心的最长（任意长度）回文串；
2. O(n)预处理后，O(1)判断一个区间是否是回文。
简介：
1. 通过插入扩展字符，使每个回文串长度都是奇数（保证有中心）
2. 记录dp[i]和当前最右回文串，若当前i<=R,则可以直接取对称位置的dp[i],加速扩展
- 这个原理+过程+复杂度和Z函数很像。
复杂度：初始化O(n)
1. 由于用dp对称位置加速，我们发现当dp[i]的右端点<R时，镜像位置左端点一定>L,那么当前位置无需继续扩展（否则对称位置也能扩展）。
2. 因此每个位置只会作为右边界被扩展成功一次，每个中心点只会扩展失败一次。因此总体是O(n)
一篇很清晰的讲解：https://leetcode.cn/problems/palindrome-partitioning-ii/solutions/369625/manacher-o1pan-duan-ren-yi-zi-chuan-shi-fou-hui-we/
例题:
1. 找最长回文串：https://leetcode.cn/problems/longest-palindromic-substring/description/
2. 计数所有回文串，注意ans += (v//2+1)//2：https://leetcode.cn/problems/palindromic-substrings/description/
3. 按回文分割，求具体方案，dp/状压枚举：https://leetcode.cn/problems/palindrome-partitioning/description/
4. 按回文分割，求最少分割数，dp+马拉车O(1)判回文：https://leetcode.cn/problems/palindrome-partitioning-ii/description/
5. O(n)分割成3个回文串，注意利用S=py或者xq的性质，hexun佬的题解：https://leetcode.cn/problems/palindrome-partitioning-iv/solutions/584373/manacherxian-xing-shi-jian-fu-za-du-by-h-sj24/
"""


class Manacher:
    def __init__(self, s):
        """马拉车用dp加速中心扩展法"""
        self.s = s
        s1 = '#' + '#'.join(s) + '#'  # 增加扩展字符
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

    def true_pre_suffix_pal(self):  # 预处理每个l为起点的最长回文'真'前缀的r(即r<n-1)和以n-1为右端点的后缀
        f, n = self.f, len(self.f) // 2
        pre, suf = list(range(n)), [n-1] * n  # pre[l]表示以l为左端点的最长回文真前缀的右端点,suf[i]表示s[i:]的最长后缀回文串的左端点，即右端点都是n-1
        for i, v in enumerate(f):
            if v > 1:  # 以i为中心存在非空回文
                l, r = (i - v // 2) >> 1, (i + v // 2 - 1) >> 1  # 这个回文串的下标
                if r == n - 1:  # 需要是最长'真'前缀，
                    suf[l] = l
                    l, r = l + 1, r - 1
                if l < n and pre[l] < r:
                    pre[l] = r
        for i in range(n - 2, -1, -1):  # 向前延伸，要么继承要么更远
            suf[i] = min(suf[i], suf[i + 1])
        for i in range(1, n):  # 如果i包含在i-1的回文串里，那么右端点可以是pre[i-1]-1
            pre[i] = max(pre[i], pre[i - 1] - 1)
        return pre, suf


# class Solution:
#     def checkPartitioning(self, s: str) -> bool:
#         n = len(s)
#         mnc = Manacher(s)
#         pre, suf = mnc.true_pre_suffix_pal()
#         for i in range(n - 2):
#             if mnc.is_palindrome(0, i):
#                 if mnc.is_palindrome(pre[i + 1] + 1, n - 1) or mnc.is_palindrome(i + 1, suf[i + 2] - 1):  # 注意+1-1
#                     return True
#         return False
#
#
# class Solution:
#     def minCut(self, s: str) -> int:
#         n = len(s)
#         # f = [[0]*n for _ in range(n)]
#         # for l in range(n-1, -1, -1):
#         #     f[l][l] = 1
#         #     if l:
#         #         f[l][l-1] = 1
#         #     for r in range(l+1, n):
#         #         if s[l] == s[r] and f[l+1][r-1]:
#         #             f[l][r] = 1
#         mnc = Manacher(s)
#         dp = [0] * (n + 1)
#         for i in range(n):
#             dp[i + 1] = dp[i] + 1
#             for j in range(i - 1, -1, -1):
#                 if mnc.is_palindrome(j, i):
#                     dp[i + 1] = min(dp[i + 1], dp[j] + 1)
#
#         return dp[-1] - 1
