
def findAnagrams(s, p):
    p = list(p)
    p.sort()
    p = ''.join(p)
    return [i for i in range(len(s)-len(p)+1) if ''.join(sorted(s[i:i+len(p)])) == p]


def findAnagrams1(s, p):
    len_s = len(s)
    len_p = len(p)
    if len_s < len_p:
        return []

    result = []
    p_count = [0] * 26
    s_count = [0] * 26

    # 统计 p 的字符频率
    for c in p:
        p_count[ord(c) - ord('a')] += 1

    # 初始化第一个窗口的字符频率
    for i in range(len_p):
        s_count[ord(s[i]) - ord('a')] += 1

    # 检查第一个窗口
    if p_count == s_count:
        result.append(0)

    # 滑动窗口
    for i in range(len_p, len_s):
        left_char = s[i - len_p]
        s_count[ord(left_char) - ord('a')] -= 1  # 左边界字符移出窗口
        right_char = s[i]
        s_count[ord(right_char) - ord('a')] += 1  # 右边界字符进入窗口
        if p_count == s_count:
            result.append(i - len_p + 1)  # 记录起始索引

    return result

if __name__ == '__main__':
    s = "cbaebabacd"
    p = "abc"
    print(findAnagrams(s, p))
    print(findAnagrams1(s, p))