class Solution(object):
    def strStr(self, haystack, needle):
        '''给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle
        字符串的第一个匹配项的下标（下标从 0 开始）。
        如果 needle 不是 haystack 的一部分，则返回  -1 '''
        if needle in haystack:
            return haystack.find(needle)
        else:
            return -1

if __name__ == '__main__':
    s = Solution()
    print(s.strStr('sadbutsad', 'sad'))


