import typing


class ZKWLazy:
    def __init__(
            self,
            op: typing.Callable[[typing.Any, typing.Any], typing.Any],
            e: typing.Any,
            mapping: typing.Callable[[typing.Any, typing.Any], typing.Any],
            composition: typing.Callable[[typing.Any, typing.Any], typing.Any],
            id_: typing.Any,
            v: typing.Union[int, typing.List[typing.Any]]) -> None:
        self._op = op  # 两段的合并，一般是+，max之类
        self._e = e  # 初始值e，一般要求任意元素x和e操作后返回值是e,例如max(x,e)=x,那么e=-inf;sum(x,e)=x,则e=0
        self._mapping = mapping  # mapping(f,x) 代表x应用f操作后的值；f:修改时进行的操作；如果是assign操作，可以lambda f,x: f if f is not None else x ,注意f是后来的，会覆盖
        self._composition = composition  # composition(f,g)两个tag的合并,即f(g(x))；如果是assign操作，可以llambda f,g: f if f is not None else g,注意f是后来的，会覆盖
        self._id = id_  # lazy默认值，一般要求f(x)=x，及应用后x不变；那种0不行的，可以设置lazy=None(或其他无效值)，然后特判

        if isinstance(v, int):
            v = [e] * v

        self._n = len(v)
        self._log = (self._n - 1).bit_length()
        self._size = 1 << self._log
        self._d = [e] * (2 * self._size)
        self._lz = [self._id] * self._size
        for i in range(self._n):
            self._d[self._size + i] = v[i]
        for i in range(self._size - 1, 0, -1):
            self._update(i)

    def set(self, p: int, x: typing.Any) -> None:
        assert 0 <= p < self._n

        p += self._size
        for i in range(self._log, 0, -1):
            self._push(p >> i)
        self._d[p] = x
        for i in range(1, self._log + 1):
            self._update(p >> i)

    def get(self, p: int) -> typing.Any:
        assert 0 <= p < self._n

        p += self._size
        for i in range(self._log, 0, -1):
            self._push(p >> i)
        return self._d[p]

    def prod(self, left: int, right: int) -> typing.Any:
        assert 0 <= left <= right <= self._n

        if left == right:
            return self._e

        left += self._size
        right += self._size

        for i in range(self._log, 0, -1):
            if ((left >> i) << i) != left:
                self._push(left >> i)
            if ((right >> i) << i) != right:
                self._push(right >> i)

        sml = self._e
        smr = self._e
        while left < right:
            if left & 1:
                sml = self._op(sml, self._d[left])
                left += 1
            if right & 1:
                right -= 1
                smr = self._op(self._d[right], smr)
            left >>= 1
            right >>= 1

        return self._op(sml, smr)

    def all_prod(self) -> typing.Any:
        return self._d[1]

    def apply(self, left: int, right: typing.Optional[int] = None,
              f: typing.Optional[typing.Any] = None) -> None:
        assert f is not None

        if right is None:
            p = left
            assert 0 <= left < self._n

            p += self._size
            for i in range(self._log, 0, -1):
                self._push(p >> i)
            self._d[p] = self._mapping(f, self._d[p])
            for i in range(1, self._log + 1):
                self._update(p >> i)
        else:
            assert 0 <= left <= right <= self._n
            if left == right:
                return

            left += self._size
            right += self._size

            for i in range(self._log, 0, -1):
                if ((left >> i) << i) != left:
                    self._push(left >> i)
                if ((right >> i) << i) != right:
                    self._push((right - 1) >> i)

            l2 = left
            r2 = right
            while left < right:
                if left & 1:
                    self._all_apply(left, f)
                    left += 1
                if right & 1:
                    right -= 1
                    self._all_apply(right, f)
                left >>= 1
                right >>= 1
            left = l2
            right = r2

            for i in range(1, self._log + 1):
                if ((left >> i) << i) != left:
                    self._update(left >> i)
                if ((right >> i) << i) != right:
                    self._update((right - 1) >> i)

    def max_right(
            self, left: int, g: typing.Callable[[typing.Any], bool]) -> int:
        assert 0 <= left <= self._n
        assert g(self._e)

        if left == self._n:
            return self._n

        left += self._size
        for i in range(self._log, 0, -1):
            self._push(left >> i)

        sm = self._e
        first = True
        while first or (left & -left) != left:
            first = False
            while left % 2 == 0:
                left >>= 1
            if not g(self._op(sm, self._d[left])):
                while left < self._size:
                    self._push(left)
                    left *= 2
                    if g(self._op(sm, self._d[left])):
                        sm = self._op(sm, self._d[left])
                        left += 1
                return left - self._size
            sm = self._op(sm, self._d[left])
            left += 1

        return self._n

    def min_left(self, right: int, g: typing.Any) -> int:
        assert 0 <= right <= self._n
        assert g(self._e)

        if right == 0:
            return 0

        right += self._size
        for i in range(self._log, 0, -1):
            self._push((right - 1) >> i)

        sm = self._e
        first = True
        while first or (right & -right) != right:
            first = False
            right -= 1
            while right > 1 and right % 2:
                right >>= 1
            if not g(self._op(self._d[right], sm)):
                while right < self._size:
                    self._push(right)
                    right = 2 * right + 1
                    if g(self._op(self._d[right], sm)):
                        sm = self._op(self._d[right], sm)
                        right -= 1
                return right + 1 - self._size
            sm = self._op(self._d[right], sm)

        return 0

    def _update(self, k: int) -> None:
        self._d[k] = self._op(self._d[2 * k], self._d[2 * k + 1])

    def _all_apply(self, k: int, f: typing.Any) -> None:
        self._d[k] = self._mapping(f, self._d[k])
        if k < self._size:
            self._lz[k] = self._composition(f, self._lz[k])

    def _push(self, k: int) -> None:
        self._all_apply(2 * k, self._lz[k])
        self._all_apply(2 * k + 1, self._lz[k])
        self._lz[k] = self._id

"""例题
区间赋值，区间求max: https://leetcode.cn/problems/falling-squares/  https://www.luogu.com.cn/problem/P3870
    tree_size = len(hashes)
    op = max  # 两个节点合并
    e = 0  # 节点初始值
    mapping = lambda f,x: f if f is not None else x  # mappint(f,x)把x节点应用f(可能是lazy),本题是如果有lazy tag，则赋值，否则不变
    composition = lambda f,g: f if f is not None else g   # 合并两个tag,如果x有值，那就应用，否则用之前的
    id_ = None  # lazy 默认值    
    tree = LazySegTree(op,e,mapping,composition,id_,tree_size)
01线段树，区间异或，区间求和：https://leetcode.cn/problems/handling-sum-queries-after-update/description/
    op = lambda x,y:(x[0]+y[0],x[1]+y[1])  # 区间长度和1的个数都是求和合并       
    e = (0, 0)  # 区间长度，1的个数
    mapping = lambda f,x: (x[0],x[0]-x[1]) if f else x  # 如果区间异或1则处理，否则不变
    composition = lambda f,g:f^g  # 合并两次异或操作     
    id_ = 0  # 默认lazytag，对异或来说就是0
    zkw = ZKWLazy(op,e,mapping,composition,id_,[(1,int(v==1)) for v in nums1])
同时存在覆盖和区间加,询问区间和：
    op = lambda x, y: (x[0] + y[0], x[1] + y[1])  # 两个节点合并
    e = (0, 1)  # 求和，节点区间长度

    def mapping(f, x):  # mapping(f,x)把x节点应用f,f[0]是覆盖,f[1]是add
        a, b = x
        if f[0] is not None:  # 如果有覆盖则优先覆盖
            a = f[0] * b
        return a + f[1] * b, b  # 如果有add则加上

    def composition(f, g):  # 合并两个tag,如果新tag是覆盖，则直接修改覆盖，add置0
        if f[0]: return f[0], 0
        return g[0], f[1] + g[1]

    id_ = (None, 0)  # lazy 默认值
    tree = ZKWLazy(op, e, mapping, composition, id_, n + 1)
维护区间内最多连续的0个数： https://www.luogu.com.cn/problem/P2894   https://leetcode.cn/problems/design-memory-allocator/
    e = (0, 0, 0, 0)  # 最多连续0，靠左的连续0，靠右的连续0,区间长度

    def op(x, y):
        mx1, l1, r1, d1 = x
        mx2, l2, r2, d2 = y
        return max(mx1, mx2, r1 + l2), l1 if l1 < d1 else l1 + l2, r2 if r2 < d2 else r2 + r1, d1 + d2

    def mapping(f, x):
        if f is None: return x
        mx, l, r, d = x
        if f == 1:
            return 0, 0, 0, d
        if f == 0:
            return d, d, d, d

    composition = lambda f, g: f if f is not None else g  # 合并
    id_ = None  # 默认lazytag
    zkw = ZKWLazy(op, e, mapping, composition, id_, [(1, 1, 1, 1) for _ in range(n)])
"""