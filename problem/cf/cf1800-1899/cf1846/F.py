# Problem: F. Rudolph and Mimic
# Contest: Codeforces - Codeforces Round 883 (Div. 3)
# URL: https://codeforces.com/contest/1846/problem/F
# Memory Limit: 256 MB
# Time Limit: 1000 ms

import sys

MOD = 10 ** 9 + 7
# MOD = 998244353
PROBLEM = """这是一个互动任务。

鲁道夫是一位研究外星生物的科学家。在鲁道夫面前有一个房间，里面散落着n个不同的物体。在这些物体中，有一种神奇的生物——模仿者，它可以变成任何物体。它已经在这个房间里假扮成了一个物体，鲁道夫需要通过实验来找到它。

实验分为几个阶段。在每个阶段，以下事情会发生：

鲁道夫观察房间里的所有物体，并记下它们的类型。每个物体的类型由一个数字表示；可能有几个相同类型的物体。
检查完毕后，鲁道夫可以指出他认为是模仿者的物体。然后实验结束。鲁道夫只有一次机会，所以如果他对模仿者的位置不确定，他会执行下一步。
鲁道夫可以从房间中移除任意数量的物体（可能为零）。然后鲁道夫离开房间，在此期间，所有物体，包括模仿者，都会互相混合，它们的顺序会改变，模仿者可以变成任何其他物体（甚至是不在房间里的物体）。
之后，鲁道夫返回房间并重复这个阶段。模仿者可能不会改变外观，但它不能连续两个阶段保持相同的物体。
鲁道夫的任务是在不超过五个阶段内检测到模仿者。

输入
第一行包含一个整数t（1≤t≤1000）——测试用例的数量。

每个测试用例的第一行包含一个整数n（2≤n≤200）——房间里的物体数量。

每个测试用例的第二行包含n个整数a1,a2,...,an（1≤ai≤9）——物体的类型。

互动
在阅读完输入数据集的描述后，你最多只能进行5次查询。读取输入数据被认为是第一个阶段的开始，而模仿者可能已经开始变化。

请求是一行。行的第一个字符表示请求类型。要移除物体，请打印“-”。然后打印数字k，表示要移除的物体数量。然后是k个数字，表示它们当前位置的物体索引。索引从1开始。你可以移除模仿者，但在这种情况下，你将无法指出它，并得到“Wrong answer”（错误答案）的判决。

对于请求，你将收到一行包含整数的回答——移除和混合后房间中剩下的物体。

要指示模仿者的位置，请打印“!”，然后打印模仿者所在物体的索引。

如果正确指出了模仿者的位置，任务将被视为解决。

如果你提出超过五个请求或者提出无效的请求，解决方案将得到“Wrong answer”（错误答案）的判决。

在输出查询或答案后，不要忘记输出行尾并刷新输出。否则，你将得到“Idleness limit exceeded”（空闲限制超过）的判决。你可以使用以下方法：

在C++中使用fflush(stdout)或cout.flush()；
在Java中使用System.out.flush()；
在Pascal中使用flush(output)；
在Python中使用stdout.flush()；
其他语言请参阅文档。

黑客攻击

你可以通过以下输入格式来黑客攻击解决方案。

第一行包含两个整数n，m（1≤m≤n≤200）——物体的数量和模仿者的位置。

第二行包含n个整数a1,a2,...,an（1≤ai≤9）——物体的初始数组。
"""

input = sys.stdin.readline


def del0():
    print('- 0')
    sys.stdout.flush()


def read():
    a = list(map(int, input().split()))
    cnt = [[] for _ in range(10)]
    for i, v in enumerate(a, start=1):
        cnt[v].append(i)
    return cnt


def diff_cnt(cnta, cntb):
    diff = 0  # 多了的种类
    tod = []  # 如果有多，其它的位置都删除
    for i in range(1, 10):
        if len(cnta[i]) < len(cntb[i]):
            diff = i
        else:
            tod.extend(cntb[i])
    return diff, tod


#       ms
def solve():
    n = int(input())
    cnta = read()
    del0()  # 第一次不删除直接读取
    cntb = read()
    while True:
        diff, tod = diff_cnt(cnta, cntb)  # 判断差异
        if diff == 0:  # 没差异就删除0个
            del0()
        else:  # 否则删除其它的
            if len(cntb[diff]) == 1:  # 多的只有1个则抓到
                print('!', cntb[diff][0])
                sys.stdout.flush()
                return
            else:
                print('-', len(tod), ' '.join(map(str, tod)))
                for i in range(1, 10):
                    if i != diff:
                        cntb[i] = []
                sys.stdout.flush()
        cnta = cntb
        cntb = read()  # 重新读取


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        solve()
