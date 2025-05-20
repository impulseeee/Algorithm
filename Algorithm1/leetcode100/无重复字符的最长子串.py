
# 错误解法
def lengthOfLongestSubstring1(s):
    """给定一个字符串 s ，请你找出其中不含有重复字符的最长子串的长度 """
    if not s:
        return 0
    if len(set(s)) == 1:
        return 1

    max_sub_length = 1
    sub_length = 1
    left = 0 # 记录每一次计数的起点
    right = 1 # 记录子串的右端点
    while right < len(s):
        if s[right] not in s[left:right]: # 字符串索引两个相同的数为空的
            sub_length += 1
        else:
            # max_sub_length = max(max_sub_length, sub_length)
            right -= 1
            left += 1
            sub_length = 1
        max_sub_length = max(max_sub_length, sub_length)
        right += 1
    return max_sub_length

def lengthOfLongestSubstring(s):
    left = max_len = 0
    pos = {}  # 记录字符最后出现的索引
    for right, char in enumerate(s):
        # 若字符在窗口内重复，左指针跳到重复位置的下一个位置
        if char in pos and pos[char] >= left:
            left = pos[char] + 1 # 窗口左指针移动到重复字符的下一个位置
        # 更新字符的最新位置
        pos[char] = right # 若当前遍历的字符没有出现过，则加入到字典中，
        # 若字符已经在之前的字典中存在过，则更新字符的最新位置

        # 计算当前窗口长度，更新最大值
        max_len = max(max_len, right - left + 1)
    return max_len





if __name__ == "__main__":
    print(lengthOfLongestSubstring("bbcd"))