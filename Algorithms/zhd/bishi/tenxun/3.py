# def FillArray(a, k):
#     b = []
#     for i in a:
#         b.append(str(i))
#     ab = ''.join(b)
#     index_0 = ab.index('0')
#     if a[index_0+1] == 0:
#
#     # write code herexion
#
#     return 1
#
# a = [0, 0, 4, 5]
# k = 6
# FillArray(a, k)
#
#
# def max_nums(str):
#     b = []
#     for i in range(len(str)):
#         b.append(str[i])

# str1 = "33322222"#'423224444'
# can = ''  # 可以看做存放元素的变量
# count = 0  # 用来判断次数
# for i in range(len(str1)):
#     if count == 0:
#         can = str1[i]
#         count += 1
#     elif str1[i] == can:
#         count += 1
#     else:
#         count -= 1
# print(can, count)

str1 = "33322222"  # '423224444'
dic = {}
for _ch in str1:
    try:
        dic[_ch] += 1
    except KeyError:
        dic[_ch] = 1
print(dic)
_res = sorted(list(dic.items()), key=lambda x: x[1])
print(_res[-1][0], _res[-1][1])

str1 = "33322222"
b = []
for ch in str1:
    a = str1.count(ch)
    b.append(a)
print(b)
print(max(b))