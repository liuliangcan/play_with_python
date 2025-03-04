# Problem: P4555 [国家集训队] 最长双回文串
# Contest: Luogu
# URL: https://www.luogu.com.cn/problem/P4555
# Memory Limit: 125 MB
# Time Limit: 1000 ms

import sys

RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())

DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')
# print = lambda d: sys.stdout.write(str(d) + "\n")  # 打开可以快写，但是无法使用print(*ans,sep=' ')这种语法,需要print(' '.join(map(str, p)))，确实会快。


PROBLEM = """最长双回文子串
用板子求出每个位置的最长真前缀，反过来求后缀，枚举分割点即可
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
        pre, suf = list(range(n)), [n - 1] * n  # pre[l]表示以l为左端点的最长回文真前缀的右端点,suf[i]表示s[i:]的最长后缀回文串的左端点，即右端点都是n-1
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


#       ms
def solve():
    s, = RS()
    a = Manacher(s)
    b = Manacher(s[::-1])
    x, y = a.true_pre_suffix_pal()[0], b.true_pre_suffix_pal()[0]
    ans = 2
    n = len(s)
    for i in range(n - 1):
        left = i + 1 if a.is_palindrome(0, i) else y[n - i - 1] - (n - i - 1) + 1
        right = n - i - 1 if a.is_palindrome(i + 1, n - 1) else x[i + 1] - i
        ans = max(ans, left + right)
    print(ans)


solve()
