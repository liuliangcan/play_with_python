"""#### 问题陈述

> 这个问题是问题 G 的简化版。

有一台有三个转盘的老虎机。
第 $i$ 个卷轴上的符号排列用字符串 $S_i$ 表示。这里，$S_i$是长度为$M$的字符串，由数字组成。

每个卷轴都有一个相应的按钮。对于每个非负整数 $t$，高桥可以选择并按下一个按钮，或者在卷轴开始转动后的第 $t$秒内什么也不做。
如果他在卷轴开始转动后的第 $t$秒按下第 $i$个卷轴对应的按钮，第 $i$个卷轴就会停止转动，并显示第 $S_i$个字符的第 $((t \bmod M)+1)$个字符。
这里，$t \bmod M$表示$t$除以$M$后的余数。

高桥希望停止所有的卷轴，这样所有显示的字符都是相同的。
请找出从旋转开始到所有卷轴停止所需的最小秒数，以便实现他的目标。
如果不可能，请报告这一事实。
"""
inf = float('inf')


def solve(s: str):
    res = [[0] * 3 for _ in range(10)]

    g = [[] for _ in range(10)]
    for i in range(len(s)):
        p = int(s[i])
        g[p].append(i)

    for i in range(10):
        # 表示不存在
        if not g[i]:
            res[i] = [inf, inf, inf]
        else:
            for j in range(3):
                res[i][j] = g[i][j % len(g[i])] + (j // len(g[i])) * len(s)

    return res


def solve_matrix(matrix) -> int:
    ans = inf
    for i in range(3):
        for j in range(3):
            if i == j:
                continue
            t = 3 - i - j

            f2 = False
            t1 = matrix[i][0]
            for s1 in range(3):
                if matrix[j][s1] > t1:
                    f2 = True
                    t1 = matrix[j][s1]
                    break

            if not f2:
                continue

            f3 = False
            for s2 in range(3):
                if matrix[t][s2] > t1:
                    f3 = True
                    t1 = matrix[t][s2]
                    break

            if f3:
                ans = min(ans, t1)

    return ans


m = int(input())
ring = []
for _ in range(3):
    ring.append(input())

r1 = solve(ring[0])
r2 = solve(ring[1])
r3 = solve(ring[2])

ans = inf
for i in range(10):
    tmp = solve_matrix([r1[i], r2[i], r3[i]])
    ans = min(ans, tmp)

print(-1 if ans == inf else ans)
