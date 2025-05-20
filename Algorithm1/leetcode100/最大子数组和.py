

"""方法思路
动态规划思想：
定义 dp[i] 为以第 i 个元素结尾的连续子数组的最大和。
状态转移方程：dp[i] = max(nums[i], dp[i-1] + nums[i])
即要么单独作为一个子数组（nums[i]），要么加入前面的子数组（dp[i-1] + nums[i]）。
优化空间复杂度：
由于 dp[i] 只依赖于 dp[i-1]，可以用一个变量 current_sum 代替数组，将空间复杂度从 O (n) 优化到 O (1)。
全局最大值：
在遍历过程中，用另一个变量 max_sum 记录所有 dp[i] 中的最大值。"""


def maxSubArray(nums):
    if not nums:
        return 0
    current_sum = max_sum = nums[0]  # 初始化为第一个元素
    for num in nums[1:]:
        # 更新当前子数组的最大和（要么单独，要么加入前面的子数组）
        current_sum = max(num, current_sum + num)
        # 更新全局最大和
        max_sum = max(max_sum, current_sum)
    return max_sum


if  __name__ == '__main__':
    nums = [1,2,-1,3]
    print(maxSubArray(nums))