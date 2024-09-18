"""位运算技巧
位运算的技巧浩如烟海，灵神的总结学不完，根本学不完0.0
用O(lgx)时间计算1~x每位上共有多少1：
    https://leetcode.cn/problems/maximum-number-that-sum-of-the-prices-is-less-than-or-equal-to-k/solutions/2603673/er-fen-da-an-shu-wei-dpwei-yun-suan-pyth-tkir/
    https://leetcode.cn/problems/find-products-of-elements-of-big-array/description/
"""


def xor1_n(n):  # 1~n的异或和
    return [n, 1, n + 1, 0][n % 4]


def cnt1onbit(x:int):  # 用O(lgx)时间计算1~x每位上共有多少1
    n = x.bit_length()  # len(bin(x))-2
    cnt = [0]*n
    for i in range(n):
        if x>>i & 1: cnt[i] += (x & ((1<<i)-1)) + 1  # 这位如果是奇数才需要计算，个数是尾缀数目
        cnt[i] += x >> (i+1) <<i  # 第二部分，x//2有多少个奇数
    return cnt
