from math import inf


def solve():
    a = list(map(int, input().split(',')))
    r = int(input())
    # print(a, r)
    f = [[-inf] * (r + 1) for _ in range(4)]
    f[0][0] = 0
    for v in a:
        for j in range(3, 0, -1):
            for k in range(r, v - 1, -1):
                f[j][k] = max(f[j][k], f[j - 1][k - v] + v)
    ans = max(f[-1])
    print(ans if ans != -inf else -1)


if __name__ == '__main__':
    solve()
