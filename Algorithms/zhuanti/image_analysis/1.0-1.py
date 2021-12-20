

class Solution:
    def numisland(self, grid):
        m = len(grid)
        n = len(grid[0])

        numisland = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    numisland += 1
                    self.dfs(grid, i, j)
        return numisland

    def dfs(self, grid, k, l):
        if (k<0 or k>=len(grid)) or (l<0 or l>=len(grid[0])) or grid[k][l] != 1:
            return
        grid[k][l] = 0
        self.dfs(grid, k-1, l)
        self.dfs(grid, k, l-1)
        self.dfs(grid, k+1, l)
        self.dfs(grid, k, l+1)


if __name__ == '__main__':
    array = [[1,1,0,0],
             [0,0,1,0],
             [1,1,0,0]]
    s = Solution()
    print(s.numisland(array))