
def solution(n):
    return int((n/3 -1 )*(n/3 -2)/2) if n%3 == 0 else 0

n = int(input())
lit = []
for i in range(n):
    # lit.append(list(map(float, input().strip().split())))  # 二维列表
    lit.append(int(input()))  # 一维列表
for j in range(n):
    # print(solution(int(lit[j][0])))  # 二维列表
    print(solution(int(lit[j])))  # 一维列表