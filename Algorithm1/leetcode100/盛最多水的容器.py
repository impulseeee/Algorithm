
def maxArea(height):  # leetcode测试的时候会超出时间限制
    max_area = 0
    for i in range(len(height)):
        for j in range(i+1, len(height)):
            area = min(height[i], height[j]) * (j-i)
            max_area = max(max_area, area)
    return max_area


def maxArea1(height):
    """
    :type height: List[int]
    :rtype: int
    """
    l, r = 0, len(height)-1
    res = 0
    while l < r:
        res = max(res, min(height[l], height[r]) * (r-l))
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return res

if __name__ == '__main__':
    height = [1,8,6,2,5,4,8,3,7]
    print(maxArea(height))