
def subarraySum(nums, k):
    count = 0
    current_sum = 0
    hash_map = {0: 1}  # 处理前缀和为 0 的情况 ？ 为什么要先处理前缀和为0的情况呢？
    for num in nums:
        current_sum += num
        target = current_sum - k
        if target in hash_map: # 计算 target = sum - k，检查 target 是否在哈希表中：
#  若存在，说明存在前缀和为 target 的子数组，其末尾索引为 i-1，则子数组 nums[i..j] 的和为 k，累加 hash_map[target] 到 count
            count += hash_map[target]
        # 更新当前前缀和的出现次数
        hash_map[current_sum] = hash_map.get(current_sum, 0) + 1
    return count

if __name__ == '__main__':
    nums = [1, 1, 1]
    k = 2
    print(subarraySum(nums, k))
