import sys

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RILST = lambda: list(RI())


class Mo:
    def __init__(self, N, Q):
        self.q = Q
        self.n = N
        self.query = [0] * Q
        self.data = [0] * Q
        self.bsize_ = int(max(1, n / max(1, (q * 2 / 3) ** 0.5)))
        # W = max(1, int(N / sqrt(Q)))

    def add_query(self, l, r, i):
        self.data[i] = l << 20 | r
        self.query[i] = ((l // self.bsize_) << 40) + ((-r if (l // self.bsize_) & 1 else r) << 20) + i

    def solve(self):
        data = self.data
        self.query.sort()
        L, R = 0, -1
        res = [0] * self.q
        mask = (1 << 20) - 1
        for lri in self.query:
            i = lri & mask
            lr = data[i]
            l, r = lr >> 20, lr & mask
            while L > l: L -= 1; add_left(L);
            while R < r: R += 1; add_right(R)
            while L < l: remove_left(L); L += 1;
            while R > r:  remove_right(R); R -= 1;
            res[i] = get()
        return res


def add_left(x):
    global cnt
    cnt += C[a[x]]
    C[a[x]] ^= 1


def add_right(x):
    global cnt
    cnt += C[a[x]]
    C[a[x]] ^= 1


def remove_left(x):
    global cnt
    C[a[x]] ^= 1
    cnt -= C[a[x]]


def remove_right(x):
    global cnt
    C[a[x]] ^= 1
    cnt -= C[a[x]]


def get():
    return cnt


n, = RI()
a = RILST()
q, = RI()

C = [0] * (n + 1)
cnt = 0
mo = Mo(n, q)
for i in range(q):
    l, r = RI()
    mo.add_query(l - 1, r - 1, i)
res = mo.solve()
print('\n'.join(map(str, res)))
