def solve1():
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))
    c = [0] * (n + 1)
    live = [1] * (n + 1)

    def add(i, v):
        while i <= n:
            c[i] += v
            i += i & -i

    def get(i):
        s = 0
        while i:
            s += c[i]
            i -= i & -i
        return s

    def kth(s):
        l, r = 0, n + 1
        while l + 1 < r:
            mid = (l + r) // 2
            if get(mid) >= s:
                r = mid
            else:
                l = mid
        return r

    for i in range(1, n + 1):
        add(i, 1)

    for v in b:
        p = kth(v)
        live[p] = 0
        add(p, -1)

    ans = [x for x, y in zip(a, live[1:]) if y]

    print(*ans)


def solve():
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))
    c = [0] * (n + 1)
    live = [1] * (n + 1)

    def add(i, v):
        while i <= n:
            c[i] += v
            i += i & -i

    def kth_upper(s):
        pos = 0
        for j in range(18, -1, -1):
            if pos + (1 << j) <= n and c[pos + (1 << j)] <= s:
                pos += (1 << j)
                s -= c[pos]
        return pos

    def kth_lower(s):
        pos = 0
        for j in range(18, -1, -1):
            if pos + (1 << j) <= n and c[pos + (1 << j)] < s:
                pos += (1 << j)
                s -= c[pos]
        return pos + 1

    for i in range(1, n + 1):
        add(i, 1)

    for v in b:
        p = kth_lower(v)
        live[p] = 0
        add(p, -1)

    ans = [x for x, y in zip(a, live[1:]) if y]

    print(*ans)


if __name__ == '__main__':
    solve()
