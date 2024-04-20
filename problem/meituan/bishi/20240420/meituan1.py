"""美团笔试题
获得s,t两个串，每次操作可以把s一个位置自增1步a->b..z->a
问能不能恰好k次操作把s变成t。
3
2 1
ab
bb
2 3
ab
bb
3 101
bbb
aaa

Yes
No
Yes
"""
"""直接贪，计算每个位置最少要多少步。d
最后剩26的倍数则可以循环掉。注意判>=0
"""


def solve():
    n, k = map(int, input().split())
    s = input()
    t = input()

    def dis(x, y):
        if x <= y:
            return ord(y) - ord(x)
        return ord(y) - ord(x) + 26

    for x, y in zip(s, t):
        k -= dis(x, y)
    if k >= 0 and k % 26 == 0:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    t = 1
    if t:
        t = int(input())
        for _ in range(t):
            solve()
    else:
        solve()


