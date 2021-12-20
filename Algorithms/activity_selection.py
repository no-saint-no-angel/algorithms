
activity = [(11, 12), (1, 4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9), (6, 10), (8, 11), (8, 12), (2, 14), (12, 16)]
# 保证活动是按照结束时间排好顺序的
activity.sort(key=lambda x:x[1])


def activity_selection(a):
    res_select = [a[0]]
    for i in range(1, len(a)):
        if a[i][0] >= res_select[-1][1]:  # 如果当前活动的开始时间大于res_select中最后一个活动的结束时间，这个当前活动就可以作为我们解的一部分
            res_select.append(a[i])
    return res_select


res_select = activity_selection(activity)
print(res_select)