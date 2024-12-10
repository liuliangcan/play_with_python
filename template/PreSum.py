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
    - 如果n方的空间受不了，但是可以接受空间n,时间nlgn，那么可以用离线+BIT二维偏序统计数点的方式做
        - 统计每个矩形里包含的点数：3382. 用点构造面积最大的矩形 II https://leetcode.cn/problems/maximum-area-rectangle-with-point-constraints-ii/description/
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


class OfflinePresum2D:
    def __init__(self, rect, points):  # rect:要统计的矩形；points:要计数的点以及贡献
        # [(x1,y1,x2,y2)..] 表示左上右下构成的矩形(保证x1<=x2&&y1<=y2)
        hy = sorted(set([p[1] for p in points] + [r[1] for r in rect] + [r[3] for r in rect]))  # 只需要把y离散化
        rect = [(x1, bisect_left(hy, y1), x2, bisect_left(hy, y2)) for x1, y1, x2, y2 in rect]
        ps = [(x, bisect_left(hy, y), v) for x, y, v in points]
        ps.sort()  # 所有障碍点
        n, m = len(hy), len(ps)
        corner = []  # 所有矩形的4个角，注意公式是s[x2,y2]+s[x1-1,y1-1]-s[x2,y1-1]-s[x1-1,y2]
        for x1, y1, x2, y2 in rect:
            corner.append((x2, y2))
            corner.append((x1 - 1, y1 - 1))
            corner.append((x2, y1 - 1))
            corner.append((x1 - 1, y2))
        corner = sorted(set(corner))  # 离线四个角，计算<=角的数点
        s = defaultdict(int)  # 缓存每个角的前缀和
        c = [0] * (n + 1)

        def add(i, v):
            while i <= n:
                c[i] += v
                i += i & -i

        def get(i):
            s = 0
            while i:
                s += c[i]
                i -= i & -i
            return s

        j = 0
        for x, y in corner:
            while j < m and (ps[j][0] < x or ps[j][0] == x and ps[j][1] <= y):
                add(ps[j][1] + 1, ps[j][2])
                j += 1
            s[x, y] = get(y + 1)
        self.cnt = [s[x2, y2] + s[x1 - 1, y1 - 1] - s[x2, y1 - 1] - s[x1 - 1, y2] for x1, y1, x2, y2 in
                    rect]  # 每个矩形里的点数



"""3382. 用点构造面积最大的矩形 II

class Solution:
    def maxRectangleArea(self, xCoord: List[int], yCoord: List[int]) -> int:
        ans = -1
        rect = []
        ps = set(zip(xCoord, yCoord))
        xy = defaultdict(list)
        yx = defaultdict(list)
        for x, y in ps:
            xy[x].append(y)
            yx[y].append(x)
        prex = defaultdict(int)
        prey = defaultdict(int)
        for x, ys in xy.items():
            for y1, y2 in pairwise(sorted(ys)):
                prey[(x, y2)] = y1
        for y, xs in yx.items():
            for x1, x2 in pairwise(sorted(xs)):
                prex[(x2, y)] = x1
        rect = []
        for x2, y2 in ps:
            x1, y1 = prex.get((x2, y2), -1), prey.get((x2, y2), -1)
            if (x1, y1) in ps:
                rect.append((x1, y1, x2, y2))
        cnt = OfflinePresum2D(rect, [(x, y, 1) for x, y in ps]).cnt

        for (x1, y1, x2, y2), c in zip(rect, cnt):
            if c == 4:
                ans = max(ans, (x2 - x1) * (y2 - y1))
        return ans
"""
