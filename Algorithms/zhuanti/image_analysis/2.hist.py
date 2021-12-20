import numpy as np


def hist(pic):
    m = len(pic)
    n = len(pic[0])
    res = np.zeros(256)
    for i in range(m):
        for j in range(n):
            a = pic[i][j]
            res[a] += 1
    return res


if __name__ == '__main__':
    array = [[1,2,3,4,5],
             [2,3,4,5,6],
             [3,4,5,6,7]]
    print(hist(array))
