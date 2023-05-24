"""
前缀和是解决离线区间和的优先思路。通过O(n)预处理可以达到O(1)询问区间和。有时和差分结合思考。
1. 朴素前缀和 pre = [0] + list(accumulate(a)),一般右移一位sum(l,r)=pre[r+1]-pre[l]
    - 结合二分
    - 结合哈希
    - 结合同余
    - 结合双(三)指针/滑窗
    - 加法/异或都支持
2. 二维前缀和
    - 难写所以打板
3. 带模前缀乘
    - 由于除法不支持同余，因此需要预处理逆元。若不预处理则需要多个O(lgn)用费马小定理实时算。
"""


class PreSum2d:
    # 二维前缀和(支持加法和异或)，只能离线使用，用n*m时间预处理，用O1查询子矩阵的和；op=0是加法，op=1是异或
    def __init__(self, g, op=0):
        m, n = len(g), len(g[0])
        self.op = op
        self.p = p = [[0] * (n + 1) for _ in range(m + 1)]
        if op == 0:
            for i in range(m):
                for j in range(n):
                    p[i + 1][j + 1] = p[i][j + 1] + p[i + 1][j] - p[i][j] + g[i][j]
        elif op == 1:
            for i in range(m):
                for j in range(n):
                    p[i + 1][j + 1] = p[i][j + 1] ^ p[i + 1][j] ^ p[i][j] ^ g[i][j]

    # O(1)时间查询闭区间左上(a,b),右下(c,d)矩形部分的数字和。
    def sum_square(self, a, b, c, d):
        if self.op == 0:
            return self.p[c + 1][d + 1] + self.p[a][b] - self.p[a][d + 1] - self.p[c + 1][b]
        elif self.op == 1:
            return self.p[c + 1][d + 1] ^ self.p[a][b] ^ self.p[a][d + 1] ^ self.p[c + 1][b]


class ModPreMul:
    """带模区间乘，O(n)预处理逆元和前缀乘，O(1)查询"""

    def __init__(self, a, p):
        """数组和模，为了防止忘记改mod，这里不设置默认值"""
        n = len(a)
        self.p = p
        self.fact = pre = [1] * (n + 1)
        self.inv = inv = [1] * (n + 1)
        for i, v in enumerate(a, start=1):
            pre[i] = pre[i - 1] * v % p

        inv[-1] = pow(pre[-1], p - 2, p)
        for i in range(n - 1, -1, -1):
            inv[i] = a[i] * inv[i + 1] % p

    def mul_interval(self, l, r):
        return self.fact[r + 1] * self.inv[l] % self.p
