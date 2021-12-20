class Solution:
    def max_area(self, grid):
        max_area_ = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    max_area_ = max(max_area_, self.dfs_zhd(i, j, grid))
        return max_area_

    def dfs_zhd(self, r, c, grid_list):
        if (r < 0 or r >= len(grid_list) or c < 0 or c >= len(grid_list[0]) or grid_list[r][c] != 1):
            return 0
        grid_list[r][c] = 0
        num_area = 1
        num_area += self.dfs_zhd(r + 1, c, grid_list)
        num_area += self.dfs_zhd(r, c + 1, grid_list)
        num_area += self.dfs_zhd(r - 1, c, grid_list)
        num_area += self.dfs_zhd(r, c - 1, grid_list)
        return num_area


if __name__ == '__main__':
    list_mine = []
    count = 0
    # while True:
    #     line = input()
    #     if line == '':
    #         break
    #     if count == 0:
    #         line = line.split('[[')
    #         line = line[1].split(']')[0]
    #         # print(line)
    #     else:
    #         line = line.split('[')
    #         # print(line)
    #         line = line[1].split(']')[0]
    #         # print(line)
    #     count += 1
    #     # print(count)
    #
    #     lines = list(map(int, line.strip().split(',')))
    #     # print(lines)
    #     list_mine.append(lines)
    str = ''
    while 1:
        try:
            str+=input()
        except:
            break
    grid = eval(str)
    print(grid)
    print(list_mine)
    s = Solution()
    print(s.max_area(list_mine))

    list_mine = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,1,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
# 0 0 1 0 0 0 0 1 0 0 0 0 0