
def twoSum(nums, target):
    d = {}
    for i in range(len(nums)):
        if (target-nums[i]) in d.keys():
            return [d[target-nums[i]], i]
        else:
            d[nums[i]] = i

if __name__ == "__main__":
    print(twoSum([2,7,11,15],18))

