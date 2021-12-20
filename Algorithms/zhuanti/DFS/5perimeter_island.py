class Solution_AC:
    def perimeterIslands(self, grid):
        perimeter_island_max = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    perimeter_island_max = max(perimeter_island_max, self.dfs(i, j, grid))
        return perimeter_island_max

    def dfs(self, r, c, grid_list):
        # print(grid_list[r][c])
        if (r < 0 or r >= len(grid_list) or c < 0 or c >= len(grid_list[0])):
            return 1
        if grid_list[r][c] == 0:
            return 1
        if grid_list[r][c] != 1:
            return 0
        grid_list[r][c] = 2
        perimeter_island = 0
        perimeter_island+=self.dfs(r + 1, c, grid_list)
        perimeter_island+=self.dfs(r, c + 1, grid_list)
        perimeter_island+=self.dfs(r - 1, c, grid_list)
        perimeter_island+=self.dfs(r, c - 1, grid_list)
        return perimeter_island

list = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
s= Solution_AC()
print(s.perimeterIslands(list))