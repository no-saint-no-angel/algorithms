import numpy as np
import random


class Noise:
    def sp_noise(self, image, prob):

        '''

        添加椒盐噪声

        prob:噪声比例

        '''

        output = np.zeros(image.shape, np.uint8)

        thres = 1 - prob

        for i in range(image.shape[0]):

            for j in range(image.shape[1]):

                rdn = random.random()

                if rdn < prob:

                    output[i][j] = 0

                elif rdn > thres:

                    output[i][j] = 255

                else:

                    output[i][j] = image[i][j]

        return output

    def gasuss_noise(self, image, mean=0, var=0.001):

        '''

            添加高斯噪声

            mean : 均值

            var : 方差

        '''

        image = np.array(image / 255, dtype=float)

        noise = np.random.normal(mean, var ** 0.5, image.shape)

        out = image + noise

        if out.min() < 0:

            low_clip = -1.

        else:

            low_clip = 0.

        out = np.clip(out, low_clip, 1.0)

        out = np.uint8(out * 255)

        # cv.imshow("gasuss", out)

        return out


class Solution:
    def filter(self, image, win_size, filter):
        image = image.transpose(1,2,0)
        ht, wt, ch = image.shape
        padding = int((win_size-1)/2)
        output = np.zeros((ht+2*padding, wt+2*padding, ch), dtype=np.float)
        output[padding:padding+ht, padding:padding+wt] = image.copy().astype(np.float)

        for h in range(ht):
            for w in range(wt):
                for c in range(ch):
                    if filter == 'mean':
                        output[padding+h, padding+w, c] = np.mean(output[h:h+win_size, w:w+win_size, c])
                    else:
                        output[padding + h, padding + w, c] = np.median(output[h:h + win_size, w:w + win_size, c])
        output = output[padding:padding+ht, padding:padding+wt]
        return output.transpose(2,0,1)

    def gaussian_filter(self, image, win_size, sigma=1.5):
        image = image.transpose(1, 2, 0)
        ht, wt, ch = image.shape
        padding = int((win_size - 1) / 2)
        output = np.zeros((ht + 2 * padding, wt + 2 * padding, ch), dtype=np.float)
        output[padding:padding + ht, padding:padding + wt] = image.copy().astype(np.float)

        # prepare kernel(小数模板）
        """
        计算平均值的时候，我们只需要将”中心点”作为原点，其他点按照其在正态曲线上的位置，分配权重，就可以得到一个加权平均值，
        而这就是上述的与二维高斯核进行卷积的过程。
        """
        """
        σ的意义及选取：
        通过上述的实现过程，不难发现，高斯滤波器模板的生成最重要的参数就是\\高斯分布的标准差σ\\
        标准差代表着数据的离散程度，从标准正太分布图中可以发现：σ越小分布越瘦高（数据越集中），σ越大分布越矮胖（数据越离散）
        如果σ较小，那么生成的模板的中心系数较大，而周围的系数较小，这样对图像的平滑效果就不是很明显；
        反之，σ较大，则生成的模板的各个系数相差就不是很大，比较类似均值模板，对图像的平滑效果比较明显。

        """
        k = np.zeros((win_size, win_size), dtype=np.float)
        for x in range(-padding, -padding+win_size):
            for y in range(-padding, -padding+win_size):
                k[y+padding, x+padding] = np.exp(-(x**2 + y**2)/(2*(sigma**2)))
        # print(k*4)
        k /= (2*np.pi*sigma*sigma)
        # print(k)
        k /= k.sum()
        # print(k)
        # filtering
        for h in range(ht):
            for w in range(wt):
                for c in range(ch):
                    output[padding+h, padding+w, c] = np.sum(k*output[h:h+win_size, w:w+win_size, c])
        output = output[padding:padding+ht, padding:padding+wt]
        return output.transpose(2,0,1)


if __name__ == '__main__':
    img = [[[1,2,3,4,5],
             [2,3,4,5,6],
             [3,4,5,6,7]],
           [[1, 2, 3, 4, 5],
            [2, 3, 4, 5, 6],
            [3, 4, 5, 6, 7]],
           [[1, 2, 3, 4, 5],
            [2, 3, 4, 5, 6],
            [3, 4, 5, 6, 7]]]
    s = Solution()
    # 添加噪声
    noise = Noise()
    img_noise = noise.gasuss_noise(np.array(img))
    print(img_noise)
    filter_list = ['mean', 'median']
    # print(s.filter(np.array(img), win_size=3, filter=filter_list[1]))
    print(s.gaussian_filter(np.array(img), win_size=3))
    print(s.gaussian_filter(np.array(img_noise), win_size=3))