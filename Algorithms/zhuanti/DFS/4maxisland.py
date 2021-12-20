class Solution_AC:
    # def maxIslands(self, grid):
    #     max_island = 0
    #     m = len(grid)
    #     n = len(grid[0])
    #     area_island = []
    #     for i in range(m):
    #         for j in range(n):
    #             if grid[i][j] == 1:
    #                 # num_island += 1
    #                 area_island.append(self.dfs(i, j, grid))
    #     # 判断area_island是否是空，有的案例全部都是0，返回的是一个空list,
    #     if area_island:
    #         return max(area_island)
    #     else:
    #         return 0

    # 再优化一下
    def maxIslands(self, grid):
        max_island = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    max_island = max(max_island, self.dfs(i, j, grid))
        return max_island

    def dfs(self, r, c, grid_list):
        """
        :param r:
        :param c:
        :param grid_list:
        :return:
        这里相对于岛屿的数量那个题，修改如下，
        1、遇到边界条件之后，需要返回岛屿面积数0，而不是直接返回None
        2、在将当前岛的节点从1变为0之后（沉岛思想），需要将面积+1，然后运用递归去遍历相邻的节点
        """
        if (r < 0 or r >= len(grid_list) or c < 0 or c >= len(grid_list[0]) or grid_list[r][c] != 1):
            return 0
        grid_list[r][c] = 0
        numarea_island = 1
        numarea_island += self.dfs(r + 1, c, grid_list)
        numarea_island += self.dfs(r, c + 1, grid_list)
        numarea_island += self.dfs(r - 1, c, grid_list)
        numarea_island += self.dfs(r, c - 1, grid_list)
        return numarea_island


if __name__ == '__main__':

    list = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
     [0,0,0,0,0,0,0,1,1,1,0,0,0],
     [0,1,1,0,1,0,0,0,0,0,0,0,0],
     [0,1,0,0,1,1,0,0,1,0,1,0,0],
     [0,1,0,0,1,1,0,0,1,1,1,0,0],
     [0,0,0,0,0,0,0,0,0,0,1,0,0],
     [0,0,0,0,0,0,0,1,1,1,0,0,0],
     [0,0,0,0,0,0,0,1,1,0,0,0,0]]

    s= Solution_AC()
    print(s.maxIslands(list))
