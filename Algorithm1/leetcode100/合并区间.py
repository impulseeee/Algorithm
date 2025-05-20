
"""方法思路
排序区间：先将所有区间按 起始点从小到大排序。这样一来，重叠的区间必然相邻，方便后续处理。
逐个合并：从第一个区间开始，依次与下一个区间比较：
如果当前区间的 结束点 ≥ 下一个区间的起始点，说明两者重叠，合并为一个新区间（起始点取较小值，结束点取较大值）。
否则，说明不重叠，将当前区间加入结果，继续处理下一个区间 """


def merge(intervals):
    if not intervals:
        return []  # 处理空输入
    # 第一步：按区间的起始点排序
    intervals.sort(key=lambda x: x[0])  # 将所有区间按起始点从小到大排序
    merged = [intervals[0]]  # 初始化结果列表，先放入第一个区间
    for current in intervals[1:]:
        last = merged[-1]  # 最后一个已合并的区间
        # 如果当前区间的起始点 ≤ 最后一个区间的结束点，说明重叠，合并
        if current[0] <= last[1]:
            # 合并后的结束点取两者的较大值
            merged[-1] = [last[0], max(last[1], current[1])]
        else:
            # 不重叠，直接加入新区间
            merged.append(current)
    return merged

if __name__ == '__main__':
    intervals = [[1,3], [2, 6], [8, 10], [15, 18]]
    print(merge(intervals))
