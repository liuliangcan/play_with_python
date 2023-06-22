from math import inf

n = int(input())
a = list(map(int, input().split()))
m = int(input())
a.sort()


# print(a)

def ok(x):
    s = 0
    p = -inf
    for v in a:
        if v - p >= x:
            s += 1
            if s >= m:
                return False
            p = v
    return True


# print(ok(4))
# print(ok(5))
# print(ok(6))
# print(ok(7))

l, r = -1, 10 ** 13
while l + 1 < r:
    mid = (l + r) // 2
    if ok(mid):
        r = mid
    else:
        l = mid
print(r - 1)
