import itertools

if __name__ == '__main__':
    n = 10 ** 5
    nums1 = [1] * (n // 2)
    nums1.extend([0] * (n // 2))
    nums2 = [10 ** 9] * n
    queries = [[1, 0, n - 1] for _ in range(n)]
    queries[1::2] = [[2, 10 ** 6, 0] for _ in range(n // 2)]
    queries[-1] = [3, 0, 0]
    print(nums1)
    print(nums2)
    print(queries)
    with open('text.txt', 'w') as f:
        f.write(str(nums1) + '\n')
        f.write(str(nums2) + '\n')
        f.write(str(queries) + '\n')
