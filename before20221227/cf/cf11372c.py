import os
import sys

if os.getenv('LOCALCFTEST'):
    sys.stdin = open('cfinput.txt')
MOD = 10 ** 9 + 7


def solve(n, a):
    correct = 0
    incorrect = -1  # 上个错误位置
    incorrect_steady = True  # 错误位置是否连续
    for i, c in enumerate(a):
        if i + 1 == c:
            correct += 1
        else:
            if incorrect != -1:
                if incorrect_steady and i != incorrect + 1:  # 不连续
                    incorrect_steady = False
            incorrect = i

    if correct == n:  # 全都在正确位置，不许操作
        return 0
    if incorrect_steady:  # 错误位置连续，直接重排这个连续子段，1次操作
        return 1
    return 2  # 错误位置不连续，无法一次搞定；直接错排整个数组，然后再有序，共需2次


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        print(solve(n, a))
