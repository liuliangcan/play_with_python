"""
矩阵快速幂，要求矩阵是正方形，可以把线性dp的O(n)优化成O(lgn)
常看常新，决定把板子弄细一点。以 LC1220. 统计元音字母序列的数目 为例
1. 把公式在纸上画出来，**注意**系数矩阵m写前边，f[i]=m*f[i-1]
        f[i][0] = f[i-1][1] + f[i-1][2] + f[i-1][4]   = [0,1,1,0,1]
        f[i][1] = f[i-1][0] + f[i-1][2]               = [1,0,1,0,0]
        f[i][2] = f[i-1][1] + f[i-1][3]               = [0,1,0,1,0]
        f[i][3] = f[i-1][2]                           = [0,0,1,0,0]
        f[i][4] = f[i-1][2] + f[i-1][3]               = [0,0,1,1,0]

2. 确定一下初始值(一般是f0或者f1)和系数要乘多少次，比如这题是f1好确定 f1=[[1],[1],[1],[1],[1]],那么fn=m^(n-1)*f1
上述可以写成 m = [矩阵]， f[i] = m * f[i-1]
        则 f[n] = m^(n-1) * f[1]
        显然f[1] = [
            [1],
            [1],
            [1],
            [1],
            [1],
        ]
3. 矩阵乘法的结果是左边矩阵的行数*右边矩阵的列数，m是正方形，所以m*f0,最后还是f的形状
4. 确定答案，比如这题是sum(fn)%MOD,但由于我们是竖着写的（f是1*k的二维矩阵）， 要写成sum(f[0] for f in fn)或者 sum(list(zip(*fn))[0]) %MOD 或者 sum(*zip(*fn)) %MOD
  但并不是所有题都取fn和的，比如斐波那契数列
例题:
1. LC70. 爬楼梯 https://leetcode.cn/problems/climbing-stairs/  斐波那契数列，临项联立
2. LC509. 斐波那契数 https://leetcode.cn/problems/fibonacci-number/ f1 = [[1], [0]]; m = [[1,1], [1,0]];return fn[0][0]
3. LC1137. 第 N 个泰波那契数  https://leetcode.cn/problems/n-th-tribonacci-number/  同上
4. LC552. 学生出勤记录 IIhttps://leetcode.cn/problems/student-attendance-record-ii/ 需要设计状态推一下线性递推关系
5. LC935. 骑士拨号器 https://leetcode.cn/problems/knight-dialer/ 每层10个状态，或者像灵神一样找本质不同的4个状态
6. LC790. 多米诺和托米诺平铺 https://leetcode.cn/problems/domino-and-tromino-tiling/ 线性dp转矩阵
7. LC1411. 给 N x 3 网格图涂色的方案数https://leetcode.cn/problems/number-of-ways-to-paint-n-3-grid/ 3进制装压（其实编码状态就行了，只有3个，可以写三重循环）+线性dp
8. LC1931. 用三种不同颜色为网格涂色 https://leetcode.cn/problems/painting-a-grid-with-three-different-colors 和上题类似，但每行长度<5,因此要装压生成状态
9. LC3337. 字符串转换后的长度 II https://leetcode.cn/problems/total-characters-in-string-after-transformations-ii/ 每个字符扩展，等于每层要记一下26个字符的数量来转移
10. LC3700. 锯齿形数组的总数 II https://leetcode.cn/problems/number-of-zigzag-arrays-ii 要前两层状态的线性dp，同样打开成1维，然后写状态转移矩阵
11. LC2851. 字符串转换 https://leetcode.cn/problems/string-transformation/ 利用kmp找出所有匹配位置，状态只有两种，i次操作后当前匹配或者不匹配
12. abc009_d 渐进式 https://atcoder.jp/contests/abc009/submissions/me 题目直接给出矩阵公式，但是递推关系是位与和异或， 注意去掉取模
13. abc236_g G - Good Vertices  https://atcoder.jp/contests/abc236/tasks/abc236_g min(max))递推


"""
from typing import List
# # 有时候这个更快, # 异或 位与模型 abc009_d
# def mul(a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
#     ret = [[0]*len(b[0]) for _ in range(len(a))]
#     for i in range(len(a)):
#         for j in range(len(b[0])):
#             for k in range(len(a[0])):
#                 ret[i][j] ^= a[i][k] & b[k][j]
#     return ret

MOD = 10**9+7

# a @ b，其中 @ 是矩阵乘法,这个不一定快
def mul(a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
    return [[sum(x * y for x, y in zip(row, col)) % MOD for col in zip(*b)]
            for row in a]

# a^n @ f1
def pow_mul(a: List[List[int]], n: int, f1: List[List[int]]) -> List[List[int]]:
    res = f1
    while n:
        if n & 1:
            res = mul(a, res)
        a = mul(a, a)
        n >>= 1
    return res
# https://leetcode.cn/problems/count-vowels-permutation/
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        """aeiou 01234
        f[i][0] = f[i-1][1] + f[i-1][2] + f[i-1][4]   = [0,1,1,0,1]
        f[i][1] = f[i-1][0] + f[i-1][2]               = [1,0,1,0,0]
        f[i][2] = f[i-1][1] + f[i-1][3]               = [0,1,0,1,0]
        f[i][3] = f[i-1][2]                           = [0,0,1,0,0]
        f[i][4] = f[i-1][2] + f[i-1][3]               = [0,0,1,1,0]
        上述可以写成 m = [矩阵]， f[i] = m * f[i-1]
        则 f[n] = m^(n-1) * f[1]
        显然f[1] = [
            [1],
            [1],
            [1],
            [1],
            [1],
        ]
        反过来
        1
        0 2
        0134
        24
        0
        """
        f1 = [
            [1],
            [1],
            [1],
            [1],
            [1],
        ]
        m = [
            [0,1,0,0,0],
            [1,0,1,0,0],
            [1,1,0,1,1],
            [0,0,1,0,1],
            [1,0,0,0,0],
        ]
        fn = pow_mul(m,n-1,f1)
        # print(fn)
        return sum(list(zip(*fn))[0]) %MOD