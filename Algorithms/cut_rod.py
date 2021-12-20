

p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]

"""
    这两种方法都是使用的递归方法。时间复杂度是O（2N）
    第一种是没有优化的方案，每次比较需要使用两次递归
    第二次有优化的方案，每次比较需要使用一次递归
"""


def cut_rod_recurision_1(p, n):
    if n == 0:
        return 0
    else:
        res = p[n]
        for i in range(1, n):
            res = max(res, cut_rod_recurision_1(p, i) + cut_rod_recurision_1(p, n-i))
        return res


def cut_rod_recurision_2(p, n):
    if n==0:
        return 0
    else:
        res = p[n]
        for i in range(1, n+1):
            res = max(res, p[i]+cut_rod_recurision_2(p, n-i))
        return res


"""
    这个是使用动态规划的思想做的，时间复杂度是O(N2)
"""


def cut_rod_dp(p, n):
    r = [0]
    for i in range(1, n+1):
        res = 0
        for j in range(1, i+1):
            res = max(res, p[j] + r[i-j])
        r.append(res)
    return r[-1]


print(cut_rod_dp(p, 9))