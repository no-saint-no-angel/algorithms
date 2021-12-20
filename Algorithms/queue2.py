

from collections import deque

# # 双向队列
# q = deque([1, 2, 3, 4, 5], 5)  # 初始化一个长度为5的队列
# q.append(6)  # 队尾进队，右边，由于队满，再次append的话，会将队列第一个弹出
# print(q)
# print(q.popleft())  # 队首弹出，左边（单向队列是pop右边出，所以这里要加popleft区分左边弹出）

# # 用于双向队列
# q.appendleft(2)  # 队首进队
# q.pop()  # 队尾出队
# print(q)

# 根据队列指定长度这个特性，可以实现打印一个文件的后面几行的功能


def tail(n):
    """
    :param n:
    :return: 返回文件的后n行
    """
    with open('test.txt', 'r') as f:
        q = deque(f, n)
        return q


for line in tail(5):
    print(line, end='')



