"""
要解决这个问题，我们可以利用 前缀积和后缀积 的思路，通过两次遍历数组分别计算每个元素左侧和右侧的乘积，
最后将两者相乘得到结果。这种方法避免了使用除法，且时间复杂度为 O (n)。
方法思路
初始化结果数组：创建一个与输入数组长度相同的结果数组 ans，初始值设为 1。
计算左侧乘积：从左到右遍历数组，记录每个元素左侧所有元素的乘积，并将结果存入 ans。例如，ans[i] 先保存左侧元素的乘积。
计算右侧乘积并合并结果：从右到左遍历数组，用一个变量 right 记录右侧元素的乘积。每次遍历将 ans[i] 乘以 right，
得到最终结果（左侧乘积 × 右侧乘积）

"""


def productExceptSelf(nums):
    n = len(nums)
    ans = [1] * n  # 初始化结果数组

    # 计算左侧乘积：ans[i] 保存 nums[0..i-1] 的乘积
    for i in range(1, n):
        ans[i] = ans[i - 1] * nums[i - 1]

    # 计算右侧乘积并合并：用 right 变量记录右侧乘积
    right = 1
    for i in range(n - 1, -1, -1):
        ans[i] *= right  # 乘以右侧乘积
        right *= nums[i]  # 更新右侧乘积（包含当前元素，供前一个元素使用）

    return ans

if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    print(productExceptSelf(nums))