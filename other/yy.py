"""
根据acw周赛92T3yy一道题：

输入n和长为n的数组a。其中1<=n,a[i]<=2e5
然后输入m(<1000)和m个操作，
每个操作包含x,y,k(k<1000)三个数，在这次操作中，你需要从a中删除值为x和y的数各一个，且向a添加一个数(x+y)。
然后输出这次操作后，数组的最大k个数的和。
题目保证输入是有效的，即每次操作时，x、y必在a中存在，且k<=len(a)。
输入:
5
1 2 3 4 5
3
1 2 2
3 3 1
6 4 2
输出:
9
6
15
解释:
第一次操作后，数组变成3 3 4 5，最大的2个数4+5=9
第二次操作后，数组变成4 5 6，最大的一个数6
第三次操作后，数组变成5 10，最大的2个数=15

# Problem: 最大数量
# Contest: AcWing
# URL: https://www.acwing.com/problem/content/description/4869/
# Memory Limit: 256 MB
# Time Limit: 1000 ms
"""
n = 5
a = [1, 2, 3, 4, 5]
m = 3
queries = [(1, 2, 2),
           (3, 3, 1),
           (6, 4, 2),
           ]

from sortedcontainers import SortedList

a = SortedList(a)
for x,y,k in queries:
    a.remove(x)
    a.remove(y)
    a.add(x+y)
    print(a)
    print(sum(a[-k:]))