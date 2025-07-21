"""几何题真是太难了

"""

""" 不用浮点数表示一条直线，
# 3625. 统计梯形的数目 II https://leetcode.cn/problems/count-number-of-trapezoids-ii/description/
一般式：Ax+By=0 
点斜式：y−y0=k(x−x0) 
斜截式：y=kx+b 
点法式：A(x−x0)+B(y−y0)=0 
应用小学学的斜截式：给出(x1,y1),(x2,y2)，那么
    斜率 k=(y2-y1)/(x2-x1)，用gcd约分一下，元组表示，注意特判dx=0的情况。另外，优先保持dx>=0，然后dy再>0
    截距 b=(y * dx - x * dy) / dx if dx else x， 但其实可以直接用b = y * dx - x * dy，因为斜率相同时，dx是相同的，这样避免除法
判断平行四边形：
对角线互相平分（共享中点），因此可以把点两两组合作为线段，存在它的中点上，那么共享中点的组内任意两条不同线段都能组成一个平行四边形（作为对角线）
"""
class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        groups = defaultdict(list)  # 斜率 -> 截距
        groups2 = defaultdict(list)  # 中点 -> 斜率

        for i, (x, y) in enumerate(points):
            for x2, y2 in points[:i]:
                dy = y - y2
                dx = x - x2
                g = gcd(abs(dx), abs(dy))
                dx //= g
                dy //= g
                if dx < 0 or dx == 0 and dy < 0:
                    dx, dy = -dx, -dy
                k = (dx, dy)
                b = y * dx - x * dy  # 截距不精确的话，不需要后边这么麻烦 (y * dx - x * dy) / dx if dx else x
                groups[k].append(b)
                groups2[(x + x2, y + y2)].append(k)

        ans = 0
        for g in groups.values():
            if len(g) == 1:
                continue
            s = 0
            for c in Counter(g).values():
                ans += s * c
                s += c

        for g in groups2.values():
            if len(g) == 1:
                continue
            s = 0
            for c in Counter(g).values():
                ans -= s * c  # 平行四边形会统计两次，减去多统计的一次
                s += c

        return ans
