'''给你两个按 非递减顺序 排列的整数数组 nums1 和 nums2，另有两个整数 m 和 n ，分别表示 nums1 和 nums2 中的元素数目。

请你 合并 nums2 到 nums1 中，使合并后的数组同样按 非递减顺序 排列。

注意：最终，合并后数组不应由函数返回，而是存储在数组 nums1 中。为了应对这种情况，nums1 的初始长度为 m + n，
其中前 m 个元素表示应合并的元素，后 n 个元素为 0 ，应忽略。nums2 的长度为 n '''

# 合并；两个有序数组，合并的结果放在原数组中，不额外增加新的数组

# 法一： 正向双指针法，会导致大量的元素移动
def merge( nums1, m, nums2, n):
    i = j = 0
    while i < m+n and j < n:
        if nums1[i] > nums2[j]:
            for k in range(m+j, i, -1):
                nums1[k] = nums1[k-1]
            nums1[i] = nums2[j]
            i += 1
            j += 1
        else:
            i += 1

    while j < n: # 只会存在这种情况了
        nums1[i-n+j] = nums2[j]
        j += 1
    return nums1

# 法二： 逆向双指针法
def merge1( nums1, m, nums2, n):
    i = m-1
    j = n-1
    k = 1

    while i >= 0 and j >= 0:   # todo 这种解法nums1中元素可能被覆盖！！
        if nums1[i] < nums2[j]:
            nums1[m+n-k] = nums2[j]
            j -= 1
            k += 1
        else:
            nums1[m+n-k] = nums1[i]
            i -= 1
            k += 1

    while i >= 0:
        nums1[m + n - k] = nums1[i]
        i -= 1
        k += 1

    while j >= 0 :
        nums1[m + n - k] = nums2[j]
        j -= 1
        k += 1



if __name__ == '__main__':
    # print(merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3))
    print(merge1(nums1 = [1], m = 1, nums2 = [], n = 0))

