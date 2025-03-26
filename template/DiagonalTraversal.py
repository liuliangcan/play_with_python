"""对角线遍历，省的现推
对角线遍历是从两条相邻边的外侧出发，到另一侧。
因此同方向对角线条数是边长即m+n-1。对这个长度拆分起点即可。
当然你可以分两次for，即：
比如遍历方向为右下的所有对角线，先遍历左边那条边，再遍历右边那条边即可。不算优雅。
这里合并

例题：
1. lc2711. 对角线上不同值的数量差 https://leetcode.cn/problems/difference-of-number-of-distinct-values-on-diagonals/description/
2. 3446. 按对角线进行矩阵排序 https://leetcode.cn/problems/sort-matrix-by-diagonals/solutions/3068709/mo-ban-mei-ju-dui-jiao-xian-pythonjavacg-pjxp/
"""


class Solution:
    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        ans = [[0] * n for _ in range(m)]

        # 第一排在右上，最后一排在左下
        # 每排从左上到右下
        # 令 k=i-j+n，那么右上角 k=1，左下角 k=m+n-1
        for k in range(1, m + n):
            # 核心：计算 j 的最小值和最大值
            min_j = 0 if k > n else n - k  # max(n - k, 0) # i=0 的时候，j=n-k，但不能是负数
            max_j = n - 1 if m > k else m + n - 1 - k  # min(m + n - 1 - k, n - 1)  # i=m-1 的时候，j=m+n-1-k，但不能超过 n-1

            st = set()
            for j in range(min_j, max_j + 1):
                i = k + j - n
                ans[i][j] = len(st)  # top_left[i][j] == len(st)
                st.add(grid[i][j])

            st = set()
            for j in range(max_j, min_j - 1, -1):
                i = k + j - n
                ans[i][j] = abs(ans[i][j] - len(st))  # bottom_right[i][j] == len(st)
                st.add(grid[i][j])
        return ans


class Solution:
    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        ans = [[0] * n for _ in range(m)]

        for i in range(m + n - 1):
            if i < m:
                x, y = m - i - 1, 0
            else:
                x, y = 0, i - m + 1
            p = set()
            while 0 <= x < m and 0 <= y < n:
                ans[x][y] = len(p)
                p.add(grid[x][y])
                x += 1
                y += 1

            if i < n:
                x, y = m - 1, i
            else:
                x, y = m - 1 - (i - n) - 1, n - 1
            p = set()
            while 0 <= x < m and 0 <= y < n:
                ans[x][y] = abs(ans[x][y] - len(p))
                p.add(grid[x][y])
                x -= 1
                y -= 1
        return ans

