from collections import deque
def maxSlidingWindow(nums, k): # 这种解法会超出时间限制
    res = []
    for i in range(len(nums) - k + 1): # 时间复杂度为O(nk),内层循环为O(k)，会执行n次
        res.append(max(nums[i:i+k]))
    return res

def maxSlidingWindow1(nums, k):
    # 利用一个双端队列（单调队列），始终保持队列内元素对应的数组值
    # 递减。这样，队列头部始终是当前窗口的最大值。具体步骤：
    #
    # 遍历数组每个元素，对每个元素：
    # 先移除队列中超出当前窗口范围的元素下标（队头）。
    # 再从队尾移除比当前元素小的下标（因为这些小值在当前元素加入后，无法再成为窗口最大值）。
    # 将当前元素下标加入队尾。
    # 当窗口形成（即下标
    # i >= k - 1）时，队列头部即为当前窗口最大值，记录该值
    q = deque()  # 双端队列存储元素下标
    res = []  # 存储结果
    for i, num in enumerate(nums):
        # 移除超出窗口范围的下标（队头）
        while q and q[0] <= i - k:
            q.popleft()
        # 从队尾移除比当前元素小的下标（保持队列递减）
        while q and nums[q[-1]] <= num:
            q.pop()
        q.append(i)
        # 当窗口形成（i >= k -1），记录队头对应的值（当前窗口最大值)，之后不管i怎么移动，只要没到终点，都会形成一个窗口，从该窗口去判断
        if i >= k - 1:
            res.append(nums[q[0]])
    return res



if __name__ == '__main__':
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    print(maxSlidingWindow(nums, k))