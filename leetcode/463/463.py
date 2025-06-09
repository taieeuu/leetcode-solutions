from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visit = set()
        m, n = len(grid), len(grid[0])
        dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        start = None
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    start = (i, j)
                    break
            if start:
                break

        def dfs(i, j):
            visit.add((i, j))
            peri = 0
            for di, dj in dir:
                ni, nj = i + di, j + dj
                if not (0 <= ni < m and 0 <= nj < n) or grid[ni][nj] == 0:
                    peri += 1
                elif grid[ni][nj]==1 and (ni, nj) not in visit:
                    peri += dfs(ni, nj)
            return peri
        if not start:
            return 0

        return dfs(*start)