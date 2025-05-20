# 给定两个字符串 s 和 t ，它们只包含小写字母。
#
# 字符串 t 由字符串 s 随机重排，然后在随机位置添加一个字母。
#
# 请找出在 t 中被添加的字母。

def findTheDifference(s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """
    t = list(t)
    for char in s:
        t.remove(char)
    return ''.join(t)

def findTheDifference1(s, t): # 采用异或运算
    exor = 0
    for ch in s+t:
        # 对字符的 Unicode 码点进行异或运算
        exor ^= ord(ch)
    return chr(exor)
# ord 函数：在循环里，使用 ord(ch) 把字符 ch 转换为对应的 Unicode 码点（整数），然后进行异或运算。
# chr 函数：异或运算结束后，使用 chr(exor) 把最终的异或结果（整数）转换回对应的字符，以符合函数返回字符串的要求。

if __name__ == '__main__':
    print(findTheDifference1('abc', 'abce'))