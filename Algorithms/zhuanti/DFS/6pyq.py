class Solution_AC:
    def numpyq(self, grid):
        num_island = 0
        visited = set()
        for i in range(len(grid)):
                if i not in visited:
                    num_island += 1
                    self.dfs(i,grid, visited)
        return num_island

    def dfs(self, i, grid_list, visited):
        for j in range(len(grid_list)):
            if (grid_list[i][j] == 1 and j not in visited):
                visited.add(j)
                self.dfs(j, grid_list,visited)

list = [[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]
s= Solution_AC()
print(s.numpyq(list))