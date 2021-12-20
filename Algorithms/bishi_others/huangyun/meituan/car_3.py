
"""
这个题目是助攻黄允美团笔试的第三道题，当时有点想法，笔试结束之后下来也没做出来，后面有时间再做吧
"""


def find_duplicated(a):
    duplicated = set()
    for i in range(0, len(a)):
        if a[i] in a[i+1:]:
            duplicated.add(a[i])
    return duplicated


def car_bao(list):
    num = int(list[0])
    weizhi_rb = []
    fx_rb = []
    for i in range(1, len(list)):
        each_rb = list(i)
        weizhi_rb.append(int(each_rb(0)))
        if each_rb(1) == 'R':
            fx_rb_small = 1
        else:
            fx_rb_small = -1
        fx_rb.append(fx_rb_small)
    time_count = 0
    output = weizhi_rb
    output1 = fx_rb
    while output1 == output:
        weizhi_rb += fx_rb
        duplicated = find_duplicated(weizhi_rb)

        output1 = output

a = [1, 2, 3, 2, 5]