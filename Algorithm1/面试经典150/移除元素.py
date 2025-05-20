
def removeElement(nums, val):
    # for i in range(len(nums)):  # 使用pop方法，会修改列表的长度，导致索引阶段出现超出范围的错误
    #     if nums[i] == val:
    #         nums.pop(i)
    # return lne(nums)

    i = 0
    while i < len(nums):  # 使用while条件不断更新列表的长度，避免数组越界
        if nums[i] == val:
            # 如果当前元素等于 val，删除该元素
            del nums[i]
        else:
            # 如果当前元素不等于 val，移动到下一个元素
            i += 1
    return len(nums)