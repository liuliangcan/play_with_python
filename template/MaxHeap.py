"""搞个最大堆"""


class MaxHeap:
    """大顶堆，py默认小顶堆，数值类型可以取相反数实现大顶堆；但str数组怎么大顶堆呢？没想到好主意，手写一个"""
    __slots__ = 'h'

    def __init__(self, h=None):
        self.h = h if h else []
        for i in reversed(range(len(self.h) // 2)):
            self._siftup(i)

    def _siftup(self, i):
        """把i位置的小数字下沉，较大的儿子提上来"""
        h = self.h
        v = h[i]
        end_pos = len(h)

        while (i << 1 | 1) < end_pos:  # 要有儿子
            child_pos = i << 1 | 1  # 左儿子
            right_pos = child_pos + 1  # 右儿子
            if right_pos < end_pos and h[child_pos] <= h[right_pos]:  # 优先上移大的那个儿子
                child_pos = right_pos
            if h[child_pos] > v:  # 这个儿子确实大，才需要上移
                h[i] = h[child_pos]
                i = child_pos
            else:  # 儿子均小就可以停了
                break
        h[i] = v

    def heappush(self, v):
        h = self.h
        h.append(v)
        i = len(h) - 1
        while i and h[(i - 1) >> 1] < v:
            h[i] = h[(i - 1) >> 1]
            i = (i - 1) >> 1
        h[i] = v

    def heappop(self):
        """把堆顶换到尾巴pop出去"""
        h = self.h
        last = h.pop()  # 如果空这里会抛异常
        if not h:
            return last
        ret, h[0] = h[0], last
        self._siftup(0)
        return ret

    def heapreplace(self, v):
        """替换并返回堆顶；用的少"""
        v, self.h[0] = self.h[0], v
        self._siftup(0)
        return v

    def heappushpop(self, v):
        """v和堆顶保留小的那个，pop更大的那个并返回；常用于保留最小的k个值(大顶堆)"""
        h = self.h
        if h and v < h[0]:
            v, h[0] = h[0], v
            self._siftup(0)
        return v

    def __len__(self):
        return len(self.h)

    def __str__(self):
        return str(self.h)


if __name__ == '__main__':
    a = [11, 12, 1, 2, 6, 3, 6, 10]
    mh = MaxHeap(a)
    mh.heappush(5)
    mh.heappush(1)
    mh.heappush(15)
    print(mh)
    while mh:
        print(mh.heappop())
