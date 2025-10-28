
import typing


class SegTreeLazy:
    """lazySegTree 0-indexed"""
    def __init__(self, op, e, mapping, composition, id_, n):
        self._op = op
        self._e = e
        self._mapping = mapping
        self._composition = composition
        self._id = id_
        self._n = n
        size = 2 << (n - 1).bit_length()
        self.val = [e for _ in range(size)]
        self.lazy = [id_ for _ in range(size)]

    def _push_lazy_to_son(self, p):
        val, lazy = self.val, self.lazy
        # if lazy[p] == self._id:return  # 这行加上性能会好，但是需要确认正确性
        l, r = p << 1, p << 1 | 1
        val[l] = self._mapping(lazy[p], val[l])
        lazy[l] = self._composition(lazy[p], lazy[l])
        val[r] = self._mapping(lazy[p], val[r])
        lazy[r] = self._composition(lazy[p], lazy[r])
        lazy[p] = self._id

    def _update_from_son(self, p):
        self.val[p] = self._op(self.val[p << 1], self.val[p << 1 | 1])

    def _apply(self, p, left, right, l, r, f):
        if left > r or right < l: return
        val, lazy = self.val, self.lazy
        if l <= left and right <= r:
            val[p] = self._mapping(f, val[p])
            lazy[p] = self._composition(f, lazy[p])
            return
        mid = (left + right) >> 1
        self._push_lazy_to_son(p)
        self._apply(p << 1, left, mid, l, r, f)
        self._apply(p << 1 | 1, mid + 1, right, l, r, f)
        self._update_from_son(p)

    def apply(self, l, r, f):  # [l,r)
        self._apply(1, 1, self._n, l+1, r, f)

    def _prod(self, p, left, right, l, r):
        if left > r or right < l:
            return self._e
        val, lazy = self.val, self.lazy
        if l <= left and right <= r:
            return val[p]
        self._push_lazy_to_son(p)
        mid = (left + right) >> 1
        return self._op(self._prod(p << 1, left, mid, l, r), self._prod(p << 1 | 1, mid + 1, right, l, r))

    def prod(self, l, r):  # [l,r)
        return self._prod(1, 1, self._n, l+1, r)

    def _set(self, p, left, right, i, v):
        val, lazy = self.val, self.lazy
        if left == right:
            val[p] = v
            return
        self._push_lazy_to_son(p)
        mid = (left + right) >> 1
        if i <= (left + right) // 2:
            self._set(p << 1, left, mid, i, v)
        else:
            self._set(p << 1 | 1, mid + 1, right, i, v)
        self._update_from_son(p)

    def set(self, i, v):
        self._set(1, 1, self._n, i+1, v)

    def _get(self, p, left, right, i):
        val, lazy = self.val, self.lazy
        if left == right:
            return val[p]
        self._push_lazy_to_son(p)
        mid = (left + right) >> 1
        if i <= ((left + right) >> 1):
            return self._get(p << 1, left, mid, i)
        return self._get(p << 1 | 1, mid + 1, right, i)

    def get(self, i):
        return self._get(1, 1, self._n, i+1)

    def _max_right(self, p, left, right, l, f, acc):
        """返回query[l,n]第一个不满足f的下标"""
        if right < l:
            return -1, self._e
        val, lazy = self.val, self.lazy
        if l <= left:
            acc2 = self._op(acc, val[p])
            if f(acc2):  # 如果整个累计上都满足，那就累上，返回-1继续向o的右兄弟找
                return -1, acc2
            if left == right:  # 如果不满足了，且只有一个，那就是它
                return left, acc
        self._push_lazy_to_son(p)
        mid = (left + right) >> 1
        pos, acc2 = self._max_right(p << 1, left, mid, l, f, acc)
        if pos != -1:
            return pos, acc20
        return self._max_right(p << 1 | 1, mid + 1, right, l, f, acc2)

    def max_right(self, l, f):
        return self._max_right(1, 1, self._n, l+1, f, self._e)[0] -1

    def _find_first_false(self, p, left, right, l, f):
        if right < l:
            return -1
        val = self.val
        if f(val[p]):
            return -1
        if left == right:
            return left
        self._push_lazy_to_son(p)
        mid = (left + right) >> 1
        pos = self._find_first_false(p << 1, left, mid, l, f)
        if pos != -1: return pos
        return self._find_first_false(p << 1 | 1, mid + 1, right, l, f)

    def find_first_false(self, l, f):  # 类似max_right,但当f不需要累计的时候，可以用
        return self._find_first_false(1, 1, self._n, l + 1, f) - 1