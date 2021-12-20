# import sys

def cl_sum(arr):
    dict_ = dict()
    res = 0
    for ele in arr:
        if ele not in dict_.keys():
            dict_[ele] = 0
        dict_[ele] += 1
    for k, v in dict_.items():
        if v == 1:
            res += k

    # new_sys2 = sorted(dict_.items(), key=lambda d: d[1], reverse=False)  # 升序
    # print(new_sys2[0][0], new_sys2[0][1])
    return res


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    print(cl_sum(arr))

