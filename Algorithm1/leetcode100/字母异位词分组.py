# 暴力破解法，超出了运行时间的限制
def groupAnagram(strs):
    res = []
    for str1 in strs:
        flag = 0
        for str2 in res:
            for str3 in str2:
                if isGroupAnagram(str3, str1):
                    flag = 1
                    str2.append(str1)
                    break
                else:
                    break
        if not flag:
            res.append([str1])
    return res

def isGroupAnagram(str1, str2):
    """ 判断两个单词是否是字母异位词 """
    if len(str1) != len(str2):
        return False

    d1 = {}
    d2 = {}
    for i in range(len(str1)):
        d1[str1[i]] = d1.get(str1[i], 0) + 1
        d2[str2[i]] = d2.get(str2[i], 0) + 1

    for k in d2.keys():
        if k not in d1.keys():
            return False
        if d1[k] != d2[k]:
            return False
    return True

# 解法二
def groupAnagram1(strs):
    d= {}
    for str1 in strs:
        key = "".join(sorted(str1)) # 对字符串进行排序, 排序后大大简化查询的次数
        if key not in d.keys():
            d[key] = [str1]
        else:
            d[key].append(str1)
    return list(d.values())





if __name__ == '__main__':
    print (groupAnagram1(["eat", "tea", "tan", "ate", "nat", "bat"]))
    print(isGroupAnagram("eat", "tea"))