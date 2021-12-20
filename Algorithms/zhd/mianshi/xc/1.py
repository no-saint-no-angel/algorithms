


def find_max(num):
    list_1 = list()
    for j in range(len(num)):
        str_copy = num.copy()
        str_copy.remove(num[j])
        tmp = ''.join(str_copy)
        list_1.append(tmp)
    return max(list_1)

if __name__ == '__main__':
    list_1 = ['1', '2', '3', '4']
    tmp = "".join(list_1)
    print(find_max(list_1))
