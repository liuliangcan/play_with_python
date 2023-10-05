# Problem: F - BOX
# Contest: AtCoder - TOYOTA SYSTEMS Programming Contest 2022(AtCoder Beginner Contest 279)
# URL: https://atcoder.jp/contests/abc279/tasks/abc279_f
# Memory Limit: 1024 MB
# Time Limit: 2000 ms

import sys
RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')
print = lambda d: sys.stdout.write(
    str(d) + "\n")  # 打开可以快写，但是无法使用print(*ans,sep=' ')这种语法,需要print(' '.join(map(str, p)))，确实会快。

MOD = 10 ** 9 + 7
# MOD = 998244353
PROBLEM = """https://atcoder.jp/contests/abc279/tasks/abc279_f

输入 n(2≤n≤3e5) 表示有 n 个盒子，编号从 1 到 n。
每个盒子都放了一个小球，其中编号为 i 的盒子放了编号为 i 的小球。

然后输入 q(1≤q≤3e5) 和 q 个操作，格式如下：
"1 x y"：把编号为 y 的盒子中的小球全部放入编号为 x 的盒子中。保证 x≠y。
"2 x"：设所有盒子中一共有 k 个小球，现在把一个新的编号为 k+1 的小球放入编号为 x 的盒子中。
"3 x"：输出编号为 x 的小球所在盒子的编号。保证 x 一定在某个盒子中。
输入
5 10
3 5
1 1 4
2 1
2 4
3 7
1 3 1
3 4
1 1 4
3 7
3 6
输出
5
4
3
1
3
"""
"""看上去是个并查集模板，但是把盒子 y 中的小球倒入盒子 x 后，盒子 y 是可以继续放入小球的。

这要怎么办？y 已经合并到 x 中了。

我们可以为 y 创建一个（大于 n 的）新的编号 z，表示一个新的空盒子。后续放入 y 的小球，就改为放在盒子 z 中。
但是这样做，要怎么输出小球所在的盒子编号呢？
记录编号为 z 的盒子的【原始盒子编号】为 y 即可。

具体细节见代码。

https://atcoder.jp/contests/abc279/submissions/46217952"""



if __name__ == '__main__':

    n, q = RI()
    # 1~n:初始小球在哪个盒子里
    # n+1~n+p:新的球在哪个盒子里
    # n+m+1~n+q:给空盒带的帽子在哪个盒子里
    fa = list(range(n + q + 2))  # 操作q次，最多出现q次(空盒子+新球)，因此n+q个位置就够用


    def find(x):
        t = x
        while fa[x] != x:
            x = fa[x]
        while t != x:
            fa[t], t = x, fa[t]
        return x


    k = n + 1  # 新球的编号
    hats = fa[:]  # 由于放球剩下的空盒子，有了帽子，实际操作帽子
    his = fa[:]  # 反向翻译，这个帽子其实是谁
    hat = n + q
    for _ in range(q):
        t, *op = RI()
        if t == 1:  # 两个帽子合并
            y, x = op
            fa[hats[x]] = hats[y]  # 倒一下这俩帽子
            hats[x] = hat  # 给空盒子一个新帽子
            his[hat] = x
            hat -= 1
        elif t == 2:
            fa[k] = hats[op[0]]  # 给新球安排到这个帽子里
            k += 1
        else:
            print(his[find(op[0])])  # 看看这个帽子其实是谁

