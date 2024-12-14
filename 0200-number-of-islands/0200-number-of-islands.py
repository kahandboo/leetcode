import sys
sys.setrecursionlimit(10**6)
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(x,y):

            if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == '0':
                return

            grid[x][y] = '0'

            dfs(x+1,y)
            dfs(x-1,y)
            dfs(x,y+1)
            dfs(x,y-1)

        m,n =  len(grid),len(grid[0])
        count = 0

        for x in range(m):
            for y in range(n):
                if grid[x][y] == '1':
                    dfs(x,y)
                    count += 1

        return count