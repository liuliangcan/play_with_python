import itertools

if __name__ == '__main__':
    # n = 10 ** 5
    # nums1 = [1] * (n // 2)
    # nums1.extend([0] * (n // 2))
    # nums2 = [10 ** 9] * n
    # queries = [[1, 0, n - 1] for _ in range(n)]
    # queries[1::2] = [[2, 10 ** 6, 0] for _ in range(n // 2)]
    # queries[-1] = [3, 0, 0]
    # print(nums1)
    # print(nums2)
    # print(queries)
    # with open('text.txt', 'w') as f:
    #     f.write(str(nums1) + '\n')
    #     f.write(str(nums2) + '\n')
    #     f.write(str(queries) + '\n')
    # p = [[range(2, 17), range(17, 32), range(32, 47), range(47, 62), range(62, 77)],
    #      [range(77, 88), range(88, 99), range(99, 110), range(110, 121), range(121, 132)],
    #      [range(132, 141), range(141, 150), range(150, 159), range(159, 168), range(168, 177)],
    #      [range(177, 184), range(184, 191), range(191, 198), range(198, 205), range(205, 212)],
    #      [range(212, 217), range(217, 222), range(222, 227), range(227, 232), range(232, 237)],
    #      [range(237, 240), range(240, 243), range(243, 246), range(246, 249), range(249, 252)],
    #      [range(252, 255), range(255, 258), range(258, 261), range(261, 264), range(264, 267)],
    #      [range(267, 269), range(269, 271), range(271, 273), range(273, 275), range(275, 277)],
    #      [range(277, 279), range(279, 281), range(281, 283), range(283, 285), range(285, 287)],
    #      [range(287, 289), range(289, 291), range(291, 293), range(293, 295), range(295, 297)]]
    # for parts in zip(*p):
    #     print(parts)
    text = ''
    with open('tools/gen_code_tool/cha.txt', 'r', encoding='utf-8') as f:
        text = f.read()
    import re

    p = re.compile(r'https://\S+[a-zA-Z0-9_]')
    cnt = 0
    for r in p.findall(text):
        print(r)
        cnt += 1
    print(cnt)

    # print(text)