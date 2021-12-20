# list = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
# print(len(list), len(list[1][0]))


list_1 = [[1,1,1,0],
          [1,0,1,0],
          [0,1,0,1]]


"""
    下面的代码是解决，给定0-1矩阵，返回连通域（4连通）的个数。
"""
class Solution:
    def numIslands(self, grid):
        num_island = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    num_island += 1
                    self.dfs(i, j, grid)
        return num_island

    def dfs(self, r, c, grid_list):
        if (r < 0 or r >= len(grid_list) or c < 0 or c >= len(grid_list[0]) or grid_list[r][c] != 1):
            return
        grid_list[r][c] = 0
        self.dfs(r + 1, c, grid_list)
        self.dfs(r, c + 1, grid_list)
        self.dfs(r - 1, c, grid_list)
        self.dfs(r, c - 1, grid_list)

s1 = Solution()
print(s1.numIslands(list_1))


"""
    这个是岛屿数量的进阶版，有三种像素值，0，1，2，0是水，1是陆地，2是有敌军的区域，求没有敌军的岛屿的数量
    思路就是将敌军区域2全部变成0，然后再求1连通域的个数
    具体步骤是：
    1、先遍历2的位置，将当前位置设置为1，然后遍历相邻的像素值位置（DFS），遍历结束之后，这个有敌军的岛屿全部变为0，消失了（沉岛）
    2、遍历剩下像素值为1的位置，求得没有敌军的岛屿的数量
"""

class Solution_stode:
    def numIslands(self, grid):
        num_island = 0
        m = len(grid)
        n = len(grid[0])
        # count_2 = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    # count_2 += 1
                    grid[i][j] = 1
                    self.dfs(i, j, grid)
        print(grid)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                # if grid[i][j] == 1 :
                #     print(grid)
                    num_island += 1
                    self.dfs(i, j, grid)
        return num_island

    def dfs(self, r, c, grid_list):
        # print(grid_list[r][c])
        if (r < 0 or r >= len(grid_list) or c < 0 or c >= len(grid_list[0]) or grid_list[r][c] != 1):
            return
        grid_list[r][c] = 0
        self.dfs(r + 1, c, grid_list)
        self.dfs(r, c + 1, grid_list)
        self.dfs(r - 1, c, grid_list)
        self.dfs(r, c - 1, grid_list)


list_2 = [[0,1,1,0],
          [2,1,1,0],
          [1,0,0,1],
          [0,1,1,1]]

s2= Solution_stode()
print(s2.numIslands(list_2))


