"""
约瑟夫环
用O(n)时间求出倒数第m个出队的人，注意仅求1个人
"""

def JosephusLastM(n, k, m):
    """约瑟夫环,n个人报数到k的人出队，问倒数第m个人的编号(1~n)"""
    winner = (k - 1) % m
    for i in range(m + 1, n + 1):
        winner = (winner + k) % i
    return winner + 1
