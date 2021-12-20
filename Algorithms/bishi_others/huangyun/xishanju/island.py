# list = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
# print(len(list), len(list[1][0]))
list = [[0,1,1,0],[2,1,1,0],[1,0,0,1],[0,1,1,1]]
# list = [[1,1,1,0],[1,0,1,0],[0,1,0,1]]


class Solution:
    def numIslands(self, grid):
        num_island = 0
        m = len(grid)
        n = len(grid[0])
        count_2 = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    count_2 += 1
                    grid[i][j] = 1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                # if grid[i][j] == 1 :
                    print(grid)
                    num_island += 1
                    self.dfs(i, j, grid)
        return num_island - count_2

    def dfs(self, r, c, grid_list):
        if (r < 0 or r >= len(grid_list) or c < 0 or c >= len(grid_list[0]) or grid_list[r][c] != 1):
            return
        grid_list[r][c] = 0
        self.dfs(r + 1, c, grid_list)
        self.dfs(r, c + 1, grid_list)
        self.dfs(r - 1, c, grid_list)
        self.dfs(r, c - 1, grid_list)

s= Solution()
print(s.numIslands(list))