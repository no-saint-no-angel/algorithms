import math

def softmax(nums):
    for i in range(len(nums)):
        nums[i] = math.exp(nums[i])
    sumcol = sum(nums)
    for i in range(len(nums)):
        nums[i] = nums[i] / float(sumcol)
    return nums
def max_num(array):
    array_sf = softmax(array)
    array_index = max(array_sf)
    array_label = array_sf.index(array_index)
    return [array_label, round(array_index, 7)]
if __name__ == '__main__':
    line_1 = input()
    N = int(line_1.split(' ')[0])#2
    K = int(line_1.split(' ')[1])#5
    input_list = []
    for i in range(N):
        temp = []
        col_ = input()
        for j in range(K):
            temp.append(float(col_.split(' ')[j]))
        input_list.append(temp)
    res = []
    for i in range(int(len(input_list))):
        ans = max_num(input_list[i])
        res.append(ans)

    num_ = int(len(res))
    for i in range(num_):
        if i == num_ - 1:
            print(str(res[i][0]) + ' ' + str(res[i][1]))
        else:
            print(str(res[i][0]) + ' ' + str(res[i][1]) + '\n')

    # 输入，input(),
    # 读取一行
    line = list(map(float, input().strip().split()))
    print(line)
    # 读取多行，指定行数
    n, m = map(int, input().strip().split())
    lit = []
    for i in range(n):
        lit.append(list(map(float, input().strip().split())))
    print(lit)
    # 读取多行，不指定行数
    lis = []
    while True:
        line = input().strip()
        if line == '':
            break
        lines = list(map(float, line.split()))
        lis.append(lines)
    print(lis)
# 2 5
# -1.739623 -4.587115 -4.286510 4.015947 -2.671629
# 2.323935 3.158164 -3.211263 2.444232 -0.413941