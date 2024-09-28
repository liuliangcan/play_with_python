"""https://orac2.info/problem/fario13maria/"""
import os.path
import sys
from math import inf

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
INFILE = ''
OUTFILE = ''
if INFILE and os.path.exists(INFILE):
    sys.stdin = open(INFILE, 'r')
if INFILE and os.path.exists(INFILE):
    sys.stdout = open(OUTFILE, 'w')
"""dp 直线上有n个硬币，k个传送站，每个站只能传一次，然后移动去拿附近的硬币。求最短移动距离。
先把和传送站重合的硬币去掉，放到一起排序。显然每个硬币一定是它附近的传送站拿。
假设ik是硬币，j是传送站。对于i--j--k来说，从j出来，要么i--j跑两遍、j--k跑一遍，然后传走；要么相反。
因此从传送站的角度出发考虑，一定是一边折返跑一边跑一次。我们即为一二型(先折返右边，再跑左边)和二一型（先折返左边再跑右边）
当i是站点时：
    记f1[i]为一二型，左边所有位置的最小答案;同理f2[i]是二一型。
    那么f1[i]由左边相邻的硬币转移而来，如果硬币是j，则是距离*1+min(f1[j-1],f2[j-1])
    f2[i]同理，距离*2+min(f1[j-1],f2[j-1])
    同时别忘了，如果左边是另一个传送站，那么不用从硬币转移，直接从上一个站转移即可。
当i是硬币时，复用这个数组：
    记f1[i]为左侧最近站点pre是一二型的答案，i作为右侧要跑两遍，即距离*2+f2[pre]
    f2[i]同理， 距离*1 + f1[pre]

"""


def solve():
    n, k = RI()
    a = set(RILST())
    b = set(RILST())
    ps = sorted(a | b)
    m = len(ps)
    t = [1] * m  # 1代表硬币
    for i, v in enumerate(ps):
        if v in b:
            t[i] = 2  # 2代表传送点

    f1 = [0] + [inf] * m  # 一二的情况
    f2 = [0] + [inf] * m  # 二一的情况
    pre1 = pre2 = inf  # 上个站点一和二的值
    pre = -inf  # 上个站点的位置
    for i, v in enumerate(ps):
        if t[i] == 2:
            f2[i + 1] = f1[i + 1] = min(f1[i], f2[i])
            for j in range(i - 1, -1, -1):
                if t[j] == 2:
                    break
                f1[i + 1] = min(f1[i + 1], ps[i] - ps[j] + min(f1[j], f2[j]))
                f2[i + 1] = min(f2[i + 1], (ps[i] - ps[j]) * 2 + min(f1[j], f2[j]))
            pre1 = f1[i + 1]
            pre2 = f2[i + 1]
            pre = v
        else:
            f1[i + 1] = (v - pre) * 2 + pre1
            f2[i + 1] = v - pre + pre2

    print(min(f1[-1], f2[-1]))


solve()

sys.stdout.close()
