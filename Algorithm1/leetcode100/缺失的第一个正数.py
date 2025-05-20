
"""要找到未排序整数数组中没有出现的最小正整数，可以利用数组索引作为标记，通过原地调整元素位置来判断每个正整数是否存在。
以下是通俗解法：
方法思路
核心思想：
将数组视为哈希表，利用索引 i 表示正整数 i+1。遍历数组时，将每个正整数 x 放到索引 x-1 的位置上。最终，第一个索引 i 处的元素不等于 i+1，则 i+1 就是缺失的最小正整数。
步骤：
调整元素位置：遍历数组，将每个值为 x 的元素（若 1 ≤ x ≤ n）交换到索引 x-1 处，确保合法正整数出现在正确位置。
查找缺失值：再次遍历数组，找到第一个索引 i 使得 nums[i] ≠ i+1，返回 i+1。若所有位置正确，返回 n+1（例如数组包含 1~n 时）。"""
def firstMissingPositive(nums):
    n = len(nums)
    # 第一步：将每个正整数放到对应的索引位置
    for i in range(n):
        while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
            # 交换 nums[i] 和 nums[nums[i]-1]
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

    # 第二步：查找第一个不匹配的索引
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1
    # 所有正整数都存在，返回 n+1
    return n + 1


if  __name__ == '__main__':
    print(firstMissingPositive([1, 2, 0]))
