import matplotlib.pyplot as plt
import numpy as np
import cv2
import time
# """
#     这个resize函数是在csd上搜的，思想是利用二分法和递归。
#     首先对高度方向进行resize，二分法就是不断地将图片二分切割，切割到，原始图片（二分切割）和需要resize(二分切割)的部分是整数倍的关系
#     如果是将原始图片放大，放大倍数是3的话，那么就是将原始图片（二分切割）复制三份得到resize(二分切割)
#     如果是将原始图片缩小，缩小倍数是3的话，那么就是将原始图片（二分切割）第i*3处的像素值赋值到resize(二分切割)图片的第i处
#     这样的赋值方式总觉得没有插值的方式好用
# """

#
# def reshape_pictures1(data,N):#改变竖直方向大小
#     n,m,d=data.shape
#     X=np.zeros([N,m,d],dtype=int)
#     if n>N:  # 缩小
#         if n%N==0:#判断是否为倍数关系，如果是可以直接修改
#             d=int(n/N)
#             for i in range(N):
#                 X[i]=data[i*d]
#             return X
#         else:
#             mid1=int(n/2)
#             mid2=int(N/2)
#             if 0<mid1:
#                 X[0:mid2]=reshape_pictures1(data[0:mid1],mid2)#递归
#             if mid1<n:
#                 X[mid2:N]=reshape_pictures1(data[mid1:n],N-mid2)#递归
#             return X
#     else:
#         if N%n==0:
#             d=int(N/n)
#             for i in range(n):
#                 for j in range(d):
#                     X[i*d+j]=data[i]
#             return X
#         else:
#             mid1=int(n/2)
#             mid2=int(N/2)
#             if 0<mid1:
#                 X[0:mid2]=reshape_pictures1(data[0:mid1],mid2)#递归
#             if mid1<n:
#                 X[mid2:N]=reshape_pictures1(data[mid1:n],N-mid2)#递归
#             return X
#
#
# def reshape_pictures2(data,M):#改变水平方向大小
#     n,m,d=data.shape
#     X=np.zeros([n,M,d],dtype=int)
#     if m>M:
#         if m%M==0:
#             d=int(m/M)
#             for i in range(M):
#                 X[:,i]=data[:,i*d]
#             return X
#         else:
#             mid1=int(m/2)
#             mid2=int(M/2)
#             if 0<mid1:
#                 X[:,0:mid2]=reshape_pictures2(data[:,0:mid1],mid2)
#             if mid1<m:
#                 X[:,mid2:M]=reshape_pictures2(data[:,mid1:m],M-mid2)
#             return X
#     else:
#         if M%m==0:
#             d=int(M/m)
#             for i in range(m):
#                 for j in range(d):
#                     X[:,i*d+j]=data[:,i]
#             return X
#         else:
#             mid1=int(m/2)
#             mid2=int(M/2)
#             if 0<mid1:
#                 X[:,0:mid2]=reshape_pictures2(data[:,0:mid1],mid2)
#             if mid1<m:
#                 X[:,mid2:M]=reshape_pictures2(data[:,mid1:m],M-mid2)
#             return X
#
# def reshape_pictures(data,N,M):#最终的修改函数
#     X=reshape_pictures1(data,N)#修改竖直方向使得大小一致
#     X=reshape_pictures2(X,M)#修改水平方向使得大小一致
#     return X
#
#
# """
#     最近邻插值
# """
#
#
# def nearest_interpolation(img, new_size):
#     dst_w, dst_h = new_size # 目标图像宽高
#     src_h, src_w = img.shape[:2] # 源图像宽高
#     scale_x = float(dst_w) / src_w # x缩放比例
#     scale_y = float(dst_h) / src_h # y缩放比例
#
#     dst_cols = (int)(img.shape[0] * scale_x)
#     dst_rows = (int)(img.shape[1] * scale_y)
#     img_dst = np.zeros([dst_cols, dst_rows, 3])
#
#     for n in range(3): # 对channel循环
#         for i in range(dst_cols - 1):
#             for j in range(dst_rows - 1):
#                 # 坐标转换
#                 scr_x = (i + 0.5) / scale_x - 0.5
#                 scr_y = (j + 0.5) / scale_y - 0.5
#
#                 # 整数部分
#                 int_x = int(scr_x)
#                 int_y = int(scr_y)
#
#                 img_dst[i, j, n] = img[int_x, int_y, n]
#
#     return img_dst
#
#
# """
#     双线性插值
# """
#
#
# def bilinear_interpolation(img, new_size):
#     dst_w, dst_h = new_size # 目标图像宽高
#     src_h, src_w = img.shape[:2] # 源图像宽高
#     scale_x = float(dst_w) / src_w # x缩放比例
#     scale_y = float(dst_h) / src_h # y缩放比例
#
#     dst_cols = (int)(img.shape[0] * scale_x)
#     dst_rows = (int)(img.shape[1] * scale_y)
#     img_dst = np.zeros([dst_cols, dst_rows, 3])
#
#     for n in range(3): # 对channel循环
#         for i in range(dst_cols - 1):
#             for j in range(dst_rows - 1):
#                 # 坐标转换
#                 scr_x = (i + 0.5) / scale_x - 0.5
#                 scr_y = (j + 0.5) / scale_y - 0.5
#
#                 # 整数部分
#                 int_x = int(scr_x)
#                 # 小数部分
#                 float_x = scr_x - int_x
#
#                 int_y = int(scr_y)
#                 float_y = scr_y - int_y
#
#                 if int_x == img.shape[0] - 1:
#                     int_x_p = img.shape[0] - 1
#                 else:
#                     int_x_p = int_x + 1
#
#                 if int_y == img.shape[1] - 1:
#                     int_y_p = img.shape[1] - 1
#                 else:
#                     int_y_p = int_y + 1
#
#                 img_dst[i, j, n] = (1 - float_x) * (1 - float_y) * img[int_x, int_y, n] + (1 - float_x) * float_y * img[int_x,
#                     int_y_p, n] + \
#                                 float_x * (1 - float_y) * img[int_x_p, int_y, n] + float_x * float_y * img[int_x_p, int_y_p, n]
#
#     return img_dst


"""
    最近邻插值另一种方法
"""


def nearst_interpolation_beta(src, new_size):
    dst_w, dst_h = new_size # 目标图像宽高
    src_h, src_w = src.shape[:2] # 源图像宽高
    if src_h == dst_h and src_w == dst_w:
        return src.copy()
    scale_x = float(dst_w) / src_w # x缩放比例
    scale_y = float(dst_h) / src_h # y缩放比例

    # 遍历目标图像，插值
    dst = np.zeros((dst_h, dst_w, 3), dtype=np.uint8)
    for n in range(3): # 对channel循环
        for dst_y in range(dst_h): # 对height循环
            for dst_x in range(dst_w): # 对width循环
                # 目标在源上的坐标（放大的话位于源位置的左上角，缩小的话位于源位置的右下角）
                src_x = (dst_x + 0.5) / scale_x - 0.5
                src_y = (dst_y + 0.5) / scale_y - 0.5
                # 计算在源图上一个近邻点的位置（在x坐标轴上，即y值不变）
                src_x_0 = int(np.round(src_x))
                src_y_0 = int(np.round(src_y))
                # src_x_1 = min(src_x_0 + 1, src_w - 1)
                # src_y_1 = min(src_y_0 + 1, src_h - 1)

                # 最近邻插值(不需要计算）
                # a = src[src_y_0, src_x_0, n]
                # value0 = (src_x_1 - src_x) * src[src_y_0, src_x_0, n] + (src_x - src_x_0) * src[src_y_0, src_x_1, n]
                # value1 = (src_x_1 - src_x) * src[src_y_1, src_x_0, n] + (src_x - src_x_0) * src[src_y_1, src_x_1, n]
                dst[dst_y, dst_x, n] = src[src_y_0, src_x_0, n]
    return dst


"""
    双线性插值另一种方法
"""


def bilinear_interpolation_beta(src, new_size):
    dst_w, dst_h = new_size # 目标图像宽高
    src_h, src_w = src.shape[:2] # 源图像宽高
    if src_h == dst_h and src_w == dst_w:
        return src.copy()
    scale_x = float(dst_w) / src_w # x缩放比例
    scale_y = float(dst_h) / src_h # y缩放比例

    # 遍历目标图像，插值
    dst = np.zeros((dst_h, dst_w, 3), dtype=np.uint8)
    for n in range(3): # 对channel循环
        for dst_y in range(dst_h): # 对height循环
            for dst_x in range(dst_w): # 对width循环
                # 目标在源上的坐标（放大的话位于源位置的左上角，缩小的话位于源位置的右下角）
                src_x = (dst_x + 0.5) / scale_x - 0.5
                src_y = (dst_y + 0.5) / scale_y - 0.5
                # 计算在源图上四个近邻点的位置（排列组合）
                src_x_0 = int(np.floor(src_x))
                src_y_0 = int(np.floor(src_y))
                src_x_1 = min(src_x_0 + 1, src_w - 1)
                src_y_1 = min(src_y_0 + 1, src_h - 1)

                # 双线性插值
                # a = src[src_y_0, src_x_0, n]
                value0 = (src_x_1 - src_x) * src[src_y_0, src_x_0, n] + (src_x - src_x_0) * src[src_y_0, src_x_1, n]
                value1 = (src_x_1 - src_x) * src[src_y_1, src_x_0, n] + (src_x - src_x_0) * src[src_y_1, src_x_1, n]
                dst[dst_y, dst_x, n] = int((src_y_1 - src_y) * value0 + (src_y - src_y_0) * value1)
    return dst


if __name__ == '__main__':
    """
        最终的测试结果只有bilinear_interpolation_beta可以使用，那就看着一种的。速度比cv2里面的慢了2000倍
    """
    img_in = cv2.imread('./pic/003615.BMP')
    start = time.time()

    img_cv2 = cv2.resize(img_in, (640,640))
    opencv_time = time.time()
    print('cv2.resize cost %f seconds' % (opencv_time - start))

    # # img_reshape_pictures = reshape_pictures(img_in, 600, 600)
    # reshape_pictures_time = time.time()
    # # print('reshape_pictures cost %f seconds' % (reshape_pictures_time - opencv_time))
    #
    # img_nearest = nearest_interpolation(img_in, (600,600))
    # nearest_time = time.time()
    # print('nearest cost %f seconds' % (nearest_time - reshape_pictures_time))
    #
    # img_bilinear = bilinear_interpolation(img_in, (600,600))
    # bilinear_time = time.time()
    # print('bilinear cost %f seconds' % (bilinear_time - nearest_time))

    nearst_beta_start_time = time.time()
    img_nearst_beta = nearst_interpolation_beta(img_in, (640,640))
    nearst_beta_time = time.time()
    print('nearst_beta cost %f seconds' % (nearst_beta_time - nearst_beta_start_time))

    bilinear_beta_start_time = time.time()
    img_bilinear_beta = bilinear_interpolation_beta(img_in, (640,640))
    bilinear_beta_time = time.time()
    print('bilinear_beta cost %f seconds' % (bilinear_beta_time - bilinear_beta_start_time))

    cv2.imshow('src_image', img_in)
    cv2.imshow('opencv_image', img_cv2)
    # cv2.imshow('reshape_pictures_image', img_reshape_pictures)
    # plt.imshow('reshape_pictures_image', img_reshape_pictures)
    # cv2.imshow('nearest_image', img_nearest)
    # cv2.imshow('img_bilinear_image', img_bilinear)
    cv2.imshow('img_nearst_beta_image', img_nearst_beta)
    cv2.imshow('img_bilinear_beta_image', img_bilinear_beta)
    cv2.waitKey()

