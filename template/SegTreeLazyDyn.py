"""lazy线段树，动态开点"""
import typing


class SegTreeLazyNode:
    """lazySegTree 0-indexed"""
    __slots__ = 'val', 'lazy', 'l', 'r', 'l_node', 'r_node'

    def __init__(self, val, lazy, l, r):
        self.val = val
        self.lazy = lazy
        self.l = l
        self.r = r
        self.l_node = None
        self.r_node = None


class SegTreeLazy:

    def __init__(self, op, e, mapping, composition, id_, n):
        self.root = SegTreeLazyNode(e, id_, 0, n - 1)
        self._op = op
        self._e = e
        self._mapping = mapping
        self._composition = composition
        self._id = id_
        self._n = n

    def _push_lazy_to_son(self, o: SegTreeLazyNode):
        left, right = o.l, o.r
        mid = (left + right) >> 1
        if o.l_node:
            l = o.l_node
            l.val = self._mapping(o.lazy, l.val)
            l.lazy = self._composition(o.lazy, l.lazy)
        else:
            o.l_node = SegTreeLazyNode(self._mapping(o.lazy, self._e), o.lazy, left, mid)
        if o.r_node:
            r = o.r_node
            r.val = self._mapping(o.lazy, r.val)
            r.lazy = self._composition(o.lazy, r.lazy)
        else:
            o.r_node = SegTreeLazyNode(self._mapping(o.lazy, self._e), o.lazy, mid + 1, right)
        o.lazy = self._id

    def _update_from_son(self, o: SegTreeLazyNode):
        o.val = self._op(o.l_node.val, o.r_node.val)

    def _build(self, o, a):
        left, right = o.l, o.r
        if left == right:
            o.val = a[left]
            o.lazy = self._id
            return
        mid = (left + right) >> 1
        o.l_node = SegTreeLazyNode(self._e, self._id, left, mid)
        o.r_node = SegTreeLazyNode(self._e, self._id, mid + 1, right)
        self._build(o.l_node, a)
        self._build(o.r_node, a)
        self._update_from_son(o)

    def build(self, a):
        self._build(self.root, a)

    def _apply(self, o: SegTreeLazyNode, l, r, f):
        left, right = o.l, o.r
        if left > r or right < l: return
        if l <= left and right <= r:
            o.val = self._mapping(f, o.val)
            o.lazy = self._composition(f, o.lazy)
            return
        self._push_lazy_to_son(o)
        self._apply(o.l_node, l, r, f)
        self._apply(o.r_node, l, r, f)
        self._update_from_son(o)

    def apply(self, l, r, f):  # [l,r)
        self._apply(self.root, l, r - 1, f)

    def _prod(self, o, l, r):
        if o:
            left, right = o.l, o.r
            if left > r or right < l:
                return self._e
            if l <= left and right <= r:
                return o.val
            self._push_lazy_to_son(o)
            return self._op(self._prod(o.l_node, l, r), self._prod(o.r_node, l, r))
        return self._e

    def prod(self, l, r):  # [l,r)
        return self._prod(self.root, l, r - 1)

    def _set(self, o, i, v):
        left, right = o.l, o.r
        # if left > i or right < i: return
        if left == right:
            o.val = v
            return
        self._push_lazy_to_son(o)
        if i <= (left + right) // 2:
            self._set(o.l_node, i, v)
        else:
            self._set(o.r_node, i, v)
        self._update_from_son(o)

    def set(self, i, v):
        self._set(self.root, i, v)

    def _get(self, o, i):
        left, right = o.l, o.r
        # if left > i or right < i: return
        if left == right:
            return o.val
        self._push_lazy_to_son(o)
        if i <= (left + right) // 2:
            return self._get(o.l_node, i)
        return self._get(o.r_node, i)

    def get(self, i):
        return self._get(self.root, i)

    def _max_right(self, o, l, f, acc):
        """返回query[l,n]第一个不满足f的下标"""
        left, right = o.l, o.r
        if right < l:
            return -1, self._e
        if l <= o.l:
            acc2 = self._op(acc, o.val)
            if f(acc2):  # 如果整个累计上都满足，那就累上，返回-1继续向o的右兄弟找
                return -1, acc2
            if o.l == o.r:  # 如果不满足了，且只有一个，那就是它
                return o.l, acc
        self._push_lazy_to_son(o)
        pos, acc2 = self._max_right(o.l_node, l, f, acc)
        if pos != -1:
            return pos, acc2
        return self._max_right(o.r_node, l, f, acc2)

    def max_right(self, l, f):
        return self._max_right(self.root, l, f, self._e)[0]
