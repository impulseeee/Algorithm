
def threeSum(nums):
    nums.sort() # 排序后就能够利用双指针进行优化
    n = len(nums)
    res = []

    for first in range(n):
        if first > 0 and nums[first] == nums[first-1]:  # 跳过重复元素
            continue
        third = n - 1  # 尾部的指针
        target = -nums[first]
        for second in range(first+1,n):  #头部的指针，通过头部指针和尾部指针进行遍历
            if second > first + 1 and nums[second] == nums[second-1]:
                continue
            while second < third and nums[second] + nums[third] > target:
                third -= 1
            if second == third:
                break
            if nums[second] + nums[third] == target: # 满足条件,两个指针指向的值为目标值
                res.append([nums[first],nums[second],nums[third]])
    return res


if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    nums1 = [-3,-3,6,0,3]
    print(threeSum(nums1))