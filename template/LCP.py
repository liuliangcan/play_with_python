"""LCP longest common prefix d
O(n^2)DP做法；用SA可以优化到On

lcp[i][j]代表s[i:]和s[j:]的最长公共前缀长度，那么只需倒序遍历，则有：
lcp[i][j]={ lcp[i+1][j+1]+1 , if s[i]==s[j]
            0               , if s[i]!=s[j]
          }
LCP在判断串内两个区间相等的时候很有用：lcp[i][j]>=d 则 s[i:i+d]==s[j;j+d]
例题： https://codeforces.com/contest/1948/problem/D
"""


class LCP:
    def __init__(self, s):
        """LCP O(n^2)做法"""
        n = len(s)
        lcp = self.lcp = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if s[i] == s[j]:
                    lcp[i][j] = lcp[i + 1][j + 1] + 1

    def is_same(self, i, j, length):
        return self.lcp[i][j] >= length


""" 有的题可以用?*等字符匹配任意字符，但可能无法优化了,只能O(n^2)DP
class LCP1:
    def __init__(self, s):
        n = len(s)
        lcp = self.lcp = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if s[i] == s[j] or s[i]=='?' or s[j] =='?':
                    lcp[i][j] = lcp[i + 1][j + 1] + 1
    def is_same(self,i,j,length):
        return self.lcp[i][j] >= length
"""
