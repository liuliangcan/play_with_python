# Problem: A. Newspaper Headline
# Contest: Codeforces - Codeforces Beta Round 75 (Div. 1 Only)
# URL: https://codeforces.com/contest/91/problem/A
# Memory Limit: 256 MB
# Time Limit: 2000 ms
#
# import sys
#
# RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
# print = lambda d: sys.stdout.write(
#     str(d) + "\n")  # 打开可以快写，但是无法使用print(*ans,sep=' ')这种语法,需要print(' '.join(map(str, p)))，确实会快。
#
# PROBLEM = """https://codeforces.com/contest/91/problem/A
#
# 输入长度不超过 1e4 的字符串 s1 和长度不超过 1e6 的字符串 s2，都只包含小写字母。
# 设字符串 t = s1 * x 表示由 s1 重复 x 次的字符串，比如 "abc" * 3 = "abcabcabc"。
# 输出使 s2 是 t 的子序列的 x 的最小值。如果无法做到输出 -1。
# 注：子序列不一定是连续的。
# 输入
# abc
# xyz
# 输出 -1
#
# 输入
# abcd
# dabc
# 输出 2
# """


# #   654    ms
# def solve():
#     s, = RS()
#     t, = RS()
#     if set(t) - set(s):  # 就是这里变成的600+ms，若用c not in set判断就可以300+
#         return print(-1)
#     n = len(s)
#     oa = ord('a')
#     dp = [[n] * 26 for _ in range(n + 1)]
#     for i in range(n - 1, -1, -1):
#         dp[i] = dp[i + 1][:]
#         dp[i][ord(s[i]) - oa] = i
#     r, ans = 0, 1
#     for c in t:
#         r = dp[r][ord(c) - oa]
#         if r == n:
#             r = dp[0][ord(c) - oa]
#             ans += 1
#         r += 1
#     print(ans)

# 248 ms
if __name__ == '__main__':
    s = input()
    t = input()
    n = len(s)
    oa = ord('a')
    # dp = [[n] * 26 for _ in range(n + 1)]
    dp = [None] * n + [[n] * 26]
    for i in range(n - 1, -1, -1):
        dp[i] = dp[i + 1][:]
        dp[i][ord(s[i]) - oa] = i

    r = ans = 0
    for c in t:
        r = dp[r][ord(c) - oa]
        if r == n:
            r = dp[0][ord(c) - oa]
            if r == n:
                print(-1)
                exit(0)
            ans += 1
        r += 1
    print(ans + 1)
