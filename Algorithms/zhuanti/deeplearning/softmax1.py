import numpy as np

def softmax(x):
    max_x = np.max(x)

    exp_x = np.exp(x-max_x)
    sum_exp_x = np.sum(exp_x)

    output = exp_x/sum_exp_x

    return output

if __name__ == '__main__':
    a = [1, 2, 3,4,5]
    print(softmax(np.array(a)))