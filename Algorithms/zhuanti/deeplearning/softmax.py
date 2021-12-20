import numpy as np
import math

class Softmax:
    def softmax(self, a):
        exp_x = np.exp(a)
        sum_exp_x = np.sum(exp_x)
        y = exp_x/sum_exp_x
        return y

    def softmax_1(self, a):
        max_exp_x = np.max(a)
        exp_x = np.exp(a-max_exp_x)
        sum_exp_x = np.sum(exp_x)
        y = exp_x/sum_exp_x
        return y


if __name__ == '__main__':
    a = [1,2,3,4,5]
    s = Softmax()
    print(s.softmax(np.array(a)))

