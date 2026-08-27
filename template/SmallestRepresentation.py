# 返回 s 的字典序最小的循环同构串
# 时间复杂度 O(|s|)，证明见代码末尾的注释
def smallestRepresentation(s: str) -> str:
    n = len(s)
    s += s
    i = 0  # 始终指向当前最小子串的首字母下标
    j = 1  # 指向需要和 i 比较的子串的首字母下标
    while j < n:
        # 暴力比较：是 i 开头的字典序小，还是 j 开头的字典序小？
        k = 0
        while k < n and s[i + k] == s[j + k]:
            k += 1
        if k >= n:
            # s 是个周期字符串，周期为 j-i
            # j+d 开头的子串等于 i+d 开头的子串，而这些子串我们之前已经排除了，继续遍历不会找到更小的
            break

        if s[i + k] < s[j + k]:  # 注：如果求字典序最大，改成 >
            # 比如从 i 开始是 "aaab"，从 j 开始是 "aaac"
            # 从 i 开始比从 j 开始更小（排除 j）
            # 此外：
            # 从 i+1 开始比从 j+1 开始更小，所以从 j+1 开始不可能是答案，排除
            # 从 i+2 开始比从 j+2 开始更小，所以从 j+2 开始不可能是答案，排除
            # ……
            # 从 i+k 开始比从 j+k 开始更小，所以从 j+k 开始不可能是答案，排除
            # 所以下一个「可能是答案」的开始位置是 j+k+1
            j += k + 1
        else:
            # 从 j 开始比从 i 开始更小，更新 i=j（也意味着我们排除了 i）
            # 此外：
            # 从 j+1 开始比从 i+1 开始更小，所以从 i+1 开始不可能是答案，排除
            # 从 j+2 开始比从 i+2 开始更小，所以从 i+2 开始不可能是答案，排除
            # ……
            # 从 j+k 开始比从 i+k 开始更小，所以从 i+k 开始不可能是答案，排除
            # 所以把 j 跳到 i+k+1，不过这可能比 j+1 小，所以与 j+1 取 max
            # 综上所述，下一个「可能是答案」的开始位置是 max(j+1, i+k+1)
            i, j = j, max(j, i + k) + 1

        # 每次要么排除 k+1 个与 i 相关的位置（这样的位置至多 n 个），要么排除 k+1 个与 j 相关的位置（这样的位置至多 n 个）
        # 所以上面关于 k 的循环，∑k <= 2n，所以二重循环的总循环次数是 O(n) 的

    return s[i: i + n]


class Solution:
    def minimumGroups(self, words: list[str]) -> int:
        st = set()

        for word in words:
            min_s = [''] * len(word)

            # 偶数下标
            s = smallestRepresentation(word[::2])
            for j, ch in enumerate(s):
                min_s[j * 2] = ch

            # 奇数下标
            s = smallestRepresentation(word[1::2])
            for j, ch in enumerate(s):
                min_s[j * 2 + 1] = ch

            st.add(''.join(min_s))

        return len(st)

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/minimum-number-of-string-groups-through-transformations/solutions/3998556/zui-xiao-biao-shi-fa-ha-xi-ji-he-qu-zhon-9tyu/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。