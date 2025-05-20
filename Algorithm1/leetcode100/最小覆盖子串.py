from collections import Counter
def minWindow(s: str, t: str) -> str:
    """
    给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。
    注意：
    对于 t 中重复字符，我们寻找的子字符串中该字符数量必须不少于 t 中该字符数量。
    如果 s 中存在这样的子串，我们保证它是唯一的答案。
    minWindow(s = "ADOBECODEBANC", t = "ABC") == "BANC" """

    if not s or not t:
        return ""

        # 统计 t 中每个字符的出现次数
    target = Counter(t)
    required = len(target)  # 需要覆盖的字符种类数,字典的键

    # 初始化窗口和计数器
    left, right = 0, 0
    formed = 0  # 当前窗口中已满足覆盖条件的字符种类数
    window_counts = {}  # 记录当前窗口中字符的出现次数

    # 记录最小窗口的长度和起始位置
    min_len = float('inf')
    min_left = 0

    while right < len(s):
        # 获取当前右指针指向的字符，并右移指针
        char = s[right]
        window_counts[char] = window_counts.get(char, 0) + 1
        right += 1

        # 检查当前字符是否在 target 中，且出现次数达到要求
        if char in target and window_counts[char] == target[char]:
            formed += 1

        # 当窗口满足覆盖条件时，尝试缩小窗口
        while left <= right and formed == required:
            char = s[left]

            # 更新最小窗口的位置和长度
            if right - left < min_len: # todo 更新最小窗口的位置和长度，除非有更小的长度，否则保持不变(<和<=结果是不一样的)
                min_len = right - left
                min_left = left

            # 移除左指针指向的字符，尝试缩小窗口
            window_counts[char] -= 1
            if char in target and window_counts[char] < target[char]:
                # 如果当前字符(需要移动的字符)在 target 中，且出现次数小于要求，则formed减1，重新移动右指针，形成窗口
                formed -= 1
            left += 1

    return "" if min_len == float('inf') else s[min_left:min_left + min_len]

if __name__ == '__main__':
    s = "ADOBAECODEBANC"
    t = "ABC"
    print(minWindow(s, t))