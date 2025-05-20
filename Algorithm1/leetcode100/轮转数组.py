def  rotate(nums, k):
    """
    给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
    >>> rotate(nums = [1,2,3,4,5,6,7], k = 3)
    [5,6,7,1,2,3,4]
    >>> rotate(nums = [-1,-100,3,99], k = 2)
    [3,99,-1,-100]
    解释：向右旋转 2 个位置后，数组变为 [] """

    # 暴力解法
    # count = 1
    # while count <= k:
    #     nums.insert(0, nums.pop())
    #     count += 1

    n = len(nums)
    k = k % n  # 处理 k 大于数组长度的情况

    # 反转整个数组
    left, right = 0, n - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

    # 反转前 k 个元素
    left, right = 0, k - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

    # 反转剩余的 n - k 个元素
    left, right = k, n - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

    return nums  # 为了便于测试，实际题目可能要求原地修改

if __name__ == '__main__':
    nums = [1,2,3,4,5,6,7]
    k = 3
    print(rotate(nums, k))

