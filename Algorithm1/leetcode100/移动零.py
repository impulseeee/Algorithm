
def moveZeroes(nums):
    # for i in range(len(nums)-1):
    #     if nums[i] == 0 and nums[i+1] != 0:
    #         nums[i], nums[i+1] = nums[i+1], nums[i]  # 这样操作是有问题的，不会改变移动后的0和其后面元素的位置，应该始终执行当前为0的元素，

    i = 0 # i指向当前第一个为0的元素
    j = i+1  # j指向当前第一个非0的元素

    while j < len(nums):
        if nums[i] != 0:
            i += 1
            j += 1
        elif nums[i] == 0 and nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j += 1
        else:
            j += 1

if __name__ == '__main__':
    nums = [0,1,0,3,12]
    moveZeroes(nums)
    print(nums)
