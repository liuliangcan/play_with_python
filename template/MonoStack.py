"""单调栈，用O(n)时间找到每个数字作为最小/最大值能管辖的区间范围"""
class MonoStack:
    # 单调栈，计算每个数作为最大/最小值值能到的前后边界。时/空复杂度O(n)
    # 注意，这里每个方法前/后遇到相同值的情况都是相反的，
    # 如果需要真实的前后边界，需要使用get_true的方法/或者调用两个函数，然后一边取l,一边取r
    def __init__(self, a):
        self.a = a

    def get_bound_as_max_left_over_and_right_stop(self):
        """使用单调递减栈，计算
        每个值作为最大值，前后能到达的边界（寻找左右第一个比它小的值）
        这里向左会越过相同值，向右会在相同值停下来。（防止重复计算区间）
        初始值为-1/n。
        """
        a, n = self.a, len(self.a)
        l, r, st = [-1] * n, [n] * n, []
        for i, v in enumerate(a):
            while st and a[st[-1]] <= v:
                r[st.pop()] = i
            if st:
                l[i] = st[-1]
            st.append(i)
        return l, r

    def get_bound_as_max_left_stop_and_right_over(self):
        """使用单调递减栈，计算
        每个值作为最大值，前后能到达的边界（寻找左右第一个比它小的值）
        这里向左会遇到相同值停下，向右会越过相同值。（防止重复计算区间）
        初始值为-1/n。
        """
        a, n = self.a, len(self.a)
        l, r, st = [-1] * n, [n] * n, []
        for i, v in enumerate(a):
            while st and a[st[-1]] < v:
                r[st.pop()] = i
            if st:
                l[i] = st[-1]
            st.append(i)
        return l, r

    def get_true_bound_as_max(self):
        # 使用单调递减栈，计算两边的真实边界(越过相同值)
        l, _ = self.get_bound_as_max_left_over_and_right_stop()
        _, r = self.get_bound_as_max_left_stop_and_right_over()
        return l, r

    def get_bound_as_min_left_over_and_right_stop(self):
        """使用单调递增栈，计算
        每个值作为最小值，前后能到达的边界（寻找左右第一个比它大的值）
        这里向左会越过相同值，向右会在相同值停下来。（防止重复计算区间）
        初始值为-1/n。
        """
        a, n = self.a, len(self.a)
        l, r, st = [-1] * n, [n] * n, []
        for i, v in enumerate(a):
            while st and a[st[-1]] >= v:
                r[st.pop()] = i
            if st:
                l[i] = st[-1]
            st.append(i)
        return l, r

    def get_bound_as_min_left_stop_and_right_over(self):
        """使用单调递增栈，计算
        每个值作为最小值，前后能到达的边界（寻找左右第一个比它大的值）
        这里向左会遇到相同值停下，向右会越过相同值。（防止重复计算区间）
        初始值为-1/n。
        """
        a, n = self.a, len(self.a)
        l, r, st = [-1] * n, [n] * n, []
        for i, v in enumerate(a):
            while st and a[st[-1]] > v:
                r[st.pop()] = i
            if st:
                l[i] = st[-1]
            st.append(i)
        return l, r

    def get_true_bound_as_min(self):
        # 使用单调递增栈，计算两边的真实边界(越过相同值)
        l, _ = self.get_bound_as_min_left_over_and_right_stop()
        _, r = self.get_bound_as_min_left_stop_and_right_over()
        return l, r

