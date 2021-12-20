import numpy as np

maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# # 使用元组来表示四个方向
# dirs = [
#     lambda x, y: (x+1, y),
#     lambda x, y: (x, y+1),
#     lambda x, y: (x-1, y),
#     lambda x, y: (x, y-1)
# ]
#
#
# def maze_path(x1, y1, x2, y2):
#     """
#     :param x1: 起始点
#     :param y1:
#     :param x2: 终点
#     :param y2:
#     :return:
#     """
#     stack = []
#     stack.append((x1, y1))
#     # 因为我们用栈来保存路径，如果栈是空的，说明没有路到达终点
#     while(len(stack)>0):
#         curNode = stack[-1]  # 表示当前路径节点
#         if curNode[0] == x2 and curNode[1] == y2:
#             # 走到终点了
#             for p in stack:
#                 print(p)
#             return True
#         for dir in dirs:  # 遍历四个方向，看哪个方向能走
#             nextNode = dir(curNode[0], curNode[1])
#             # 如果下一个节点能走，压入栈
#             if maze[nextNode[0]][nextNode[1]] == 0:
#                 stack.append(nextNode)
#                 maze[nextNode[0]][nextNode[1]] = 2  # 2表示已经走过
#                 break  # 有一个方向能走就跳出for循环，继续while循环，把最后一个节点当作是当前节点
#         else:  # 循环之后发现，四个方向都不能走，那就把栈顶元素弹出，原路返回，寻找有方向可以走的节点
#             # maze[nextNode[0]][nextNode[1]] = 2
#             # 往回退一个
#             stack.pop()
#
#     else:  # while循环跳出，说明栈空，无路可走
#         print("没有路！")
#         return False
#
#     return stack


# stack = maze_path(1, 1, 8, 8)
# print(stack)


# 迷宫的当前节点的四个方向
dirs = [
    lambda x, y:(x+1, y),
    lambda x, y:(x, y+1),
    lambda x, y:(x-1, y),
    lambda x, y:(x, y-1)
]


def maze_path_test(x1, y1, x2, y2):
    """
    :param x1:
    :param y1:
    :param x2:
    :param y2:
    :return:
    """
    stack = []
    stack.append((x1, y1))
    # 设置一个while循环，结束条件就是栈空
    while len(stack) > 0:
        curNode = stack[-1]
        # 判断当前节点是否是终点
        if curNode[0]==x2 and curNode[1]==y2:
            # 打印路径
            print("此迷宫的路径是：")
            for p in stack:
                print(p)
            return True
        else:
            # 遍历当前节点的四个方向，看看是否有方向可以走通
            for dir in dirs:
                nextNode = dir(curNode[0], curNode[1])
                if maze[nextNode[0]][nextNode[1]] == 0:  # 如果有一个方向可以走通，那就把nextNode压入栈，并标记该节点已经走过，退出循环，重新开始while循环
                    stack.append((nextNode[0], nextNode[1]))
                    maze[nextNode[0]][nextNode[1]] = 2
                    break
            # 如果循环结束之后，四个方向均不能走，说明当前节点（栈顶节点）无路可走，原路返回
            else:
                stack.pop()
    else:
        print("此迷宫没有路！")
        return False


stack = maze_path_test(1, 1, 8, 8)
print(stack)