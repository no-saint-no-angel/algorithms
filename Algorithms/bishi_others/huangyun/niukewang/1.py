

def yinzidu(arr):
    num = len(arr)
    ans_set = [0 for i in range(num)]
    for i in range(num):
        for j in range(i, num):
            if arr[j]%arr[i] == 0:
                ans_set[i] += 1

    arr_num_index = ans_set.index(max(ans_set))
    out_set = [0 for i in range(arr[arr_num_index]+1)]

    for i in range(2, arr[arr_num_index]+1):
        for j in range(num):
            if arr[j]%i == 0:
                out_set[i] += 1
    print(out_set)
    return out_set.index(max(out_set))


if __name__ == '__main__':
    input_arr = [8,9,18,90,72]
    # input_arr = sorted(input_arr)
    print(yinzidu(input_arr))
