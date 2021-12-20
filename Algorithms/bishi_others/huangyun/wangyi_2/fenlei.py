# import numpy as np
import math
class Solution():

    # def softmax2(self, x):
    #     """Compute softmax values for each sets of scores in x."""
    #     x = np.array(x)
    #     x = np.exp(x)
    #     if x.ndim == 1:
    #         sumcol = sum(x)
    #         for i in range(x.size):
    #             x[i] = x[i]/float(sumcol)
    #     if x.ndim > 1:
    #         sumcol = x.sum(axis=0)
    #         for row in x:
    #             for i in range(row.size):
    #                 row[i] = row[i]/float(sumcol[i])
    #     return x

    def softmax3(self, x):
        """Compute softmax values for each sets of scores in x."""
        # x = np.array(x)
        # x = np.exp(x)
        for i in range(len(x)):
            x[i] = math.exp(x[i])
        sumcol = sum(x)
        for i in range(len(x)):
            x[i] = x[i]/float(sumcol)
        # if x.ndim > 1:
        #     sumcol = x.sum(axis=0)
        #     for row in x:
        #         for i in range(row.size):
        #             row[i] = row[i]/float(sumcol[i])
        return x

    def max_num(self, array):
        array_sf = self.softmax3(array)
        # array_index = array_sf.argmax(axes=0)
        array_index = max(array_sf)
        array_leibie = array_sf.index(array_index)
        # array_leibie = np.where(array_sf==array_index)
        return [array_leibie, round(array_index, 6)]
        # print(array_leibie, array_index)


if __name__ == '__main__':
    array_a = [1, 2, 3, 5]
    max_e = Solution()
    output = max_e.max_num(array_a)
    print(output)


# d1 = {1:'food'}
# d2 = {1:'食品', 2:'饮料'}
# d1.update(d2)
# print(d1[1])

# s = 'ajldjlajfdljfccc'
# s = set(s)
# s = list(s)
# s.sort()
# res = "".join(s)
# print(res)

