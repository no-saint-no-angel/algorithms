from collections import deque

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

dirs = [
    lambda x,y:(x+1, y),
    lambda x,y:(x-1, y),
    lambda x,y:(x, y-1),
    lambda x,y:(x, y+1)
]


# def pri_path(path):
#
#     curNode = path[-1]
#     realpath = []
#     while curNode[2] != -1:
#         realpath.append(curNode[0:2])
#         curNode = path[curNode[2]]
#
#     realpath.append(curNode[0:2])  # 把起点放进去
#     realpath.reverse()
#     for node in realpath:
#         print(node)
#
#
# def maze_path_queue(x1, y1, x2, y2):
#     queue_0 = deque()
#     queue_0.append((x1, y1, -1))
#     path = []
#     while len(queue_0)>0:
#         curNode = queue_0.popleft()
#         path.append(curNode)
#         if curNode[0] == x2 and curNode[1] == y2:
#             print(pri_path(path))
#             return True
#         else:
#             for dir in dirs:
#                 nextNode = dir(curNode[0], curNode[1])
#                 if maze[nextNode[0]][nextNode[1]] == 0:
#                     queue_0.append((nextNode[0], nextNode[1], len(path)-1))  # 这里的len(path)-1表明的是前一个节点的位置，即谁把nextNode带过来的
#                     maze[nextNode[0]][nextNode[1]] = 2
#     else:
#         print("没有路！")
#         return False


def pri_path_test(path):
    curNode = path[-1]  # path中的最后一个节点就是终点
    realpath = []
    while curNode[2] != -1:  # 只要curNode不是起始点，那从最后一个节点（终点）开始往前索引终点都是由哪些节点过来的
        realpath.append(curNode[0:2])
        curNode = path[curNode[2]]  # 根据当前节点储存的上一个节点在path中的位置信息，找到上一个节点，（更新）令做当前节点，继续循环，直到realpath把终点到起点之间的节点都储存起来
    # 循环结束之后，除了起始点之外，路径上的所有点都在realpath中
    realpath.append(curNode[0:2])
    realpath.reverse()
    for node in realpath:
        print(node)


def maze_path_queue_test(x1, y1, x2, y2):
    queue_1 = deque()
    queue_1.append((x1, y1, -1))
    path = []

    while len(queue_1) > 0:
        curNode = queue_1.popleft()
        path.append(curNode)
        if curNode[0]==x2 and curNode[1]==y2:
            print("迷宫的路径如下：")
            pri_path_test(path)
            return True

        else:
            for dir in dirs:
                nextNode=dir(curNode[0], curNode[1])
                if maze[nextNode[0]][nextNode[1]]==0:
                    queue_1.append((nextNode[0], nextNode[1], len(path)-1))
                    maze[nextNode[0]][nextNode[1]]=2

    else:
        print("没有路！")
        return False


maze_path_queue_test(1,1,8,8)