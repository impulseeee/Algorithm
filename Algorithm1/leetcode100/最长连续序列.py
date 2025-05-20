
def longestConsecutivedef(nums):
    if not nums: # 如果nums为空，则返回0
        return 0
    nums.sort() # 排序后去统计，但是会导致时间复杂度为O(nlogn)
    res = 1
    count = 1
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
            continue
        if nums[i] == nums[i-1] + 1:
            count += 1
        else:
            count = 1
        res = max(res, count)
    return res


def longestConsecutivedef1(nums): # 有问题的解法
    if not nums:
        return 0
    d = {}
    for num in nums:
        if num-1 not in d.keys():
            d[num] = d.get(num+1, 0) + 1
        else:
            d[num] = d.get(num-1, 0) + 1
    return max(d.values())


def longestConsecutivedef3(nums):
    """" 该函数用于找出列表中连续数字的最长序列长度。
将输入列表转为集合以提高查找效率；
遍历集合中的每个数字，仅当该数字是连续序列的起始值时（即num-1不在集合中），
开始向后检查连续递增序列；
统计当前连续序列长度，并更新最长序列记录；
最终返回最长连续序列长度 """
    longest_streak = 0
    num_set = set(nums)
    for num in num_set:
        if num - 1 not in num_set: # 仅当该数字是连续序列的起始值时
            concurrent_num = num
            streak = 1
            while concurrent_num + 1 in num_set:  # 向后检查连续递增序列，只会检查一次，只有一个元素符合
                concurrent_num += 1
                streak += 1
            longest_streak = max(longest_streak, streak)
    return longest_streak

if  __name__ == '__main__':
    nums = [100,4,200,1,3,2]
    print(longestConsecutivedef3(nums))

