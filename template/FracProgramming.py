"""分数规划(01分数规划)
通用描述：给出a[i],b[i],求一组w[i] in {0,1},最大化或最小化sum{a[i]*w[i]}/sum{b[i]*w[i]}
另一种描述：每个物品有两个权值a[i],b[i],选出一组物品，最大/最小化sum{a}/sum{b}。
一般分数规划还有些奇怪的限制，比如“分母至少为W”

分数规划的通用解法是二分。
通过二分答案的方法，增加一个条件avg，使得check问题变成一个维度.
比如单纯的求最大化一组数据的平均数，那么可以使每个v偏移avg变成t=v-avg,那么t>=0则是可选的。
更通用的，可以推公式:
        sum{ai*wi}/sum{bi*wi} > mid
    =>  sum{ai*wi} - mid * sum{bi*wi} > 0
    =>  sum{wi*(ai-mid*bi)} > 0
    即，每个位置变成t=ai-mid*bi,讨论这个值的选或不选
浮点数二分可以直接循环固定次数60次，或者定义eps=1e-7,写while r-l>eps: ...

分数规划的难点一般在于推出式子后，求sum{wi*(ai-mid*bi)} 的最大最小值，即写check

关于二分边界：通常可以l,r=0,10**15。
        但有时可以更紧：
            l 看题目是否可以都选 sum(a)/sum(b)；或者选一段至少长度为k的sum(a[:k])/sum(b[:k])
            r 如果存在最大的ai/bi,那么加上别的不可能变得更大。

例题：
    - 01背包,限制分母至少为w，P4377 [USACO18OPEN] Talent Show G  https://www.luogu.com.cn/problem/P4377
    - lc644(会员题), 求最大子段平均值(长度不少于k)， x-avg，转化成长度不小于k的最大子段和
    - 分数规划结合dp https://atcoder.jp/contests/abc324/tasks/abc324_f


其他：有的题目要求把答案乘1000输出，可以一开始就把分母*1000.
    有的要求取整，但是如果答案恰好是整数x，由于浮点数精度误差最后可能得到一个x-0.00..001，取整后就是x-1。避免这个可以把答案加一个eps。
"""



def solve():
    n, w = RI()
    a = []
    for _ in range(n):
        x, y = RI()
        a.append((x, y * 1000))
    eps=1e-2
    def ok(x):
        f = [0] + [-inf] * w
        for v, t in a:
            for j in range(w, -1, -1):
                p = min(w, j + v)
                f[p] = max(f[p], f[j] + t - x * v)
        return f[-1] <= 0

    l, r = sum(x for x, _ in a) / sum(y for _, y in a), max(y / x for x, y in a) + 1
    # for _ in range(60):
    while r - l > eps:
        mid = (l + r) / 2
        if ok(mid):
            r = mid
        else:
            l = mid
    print(int(r))