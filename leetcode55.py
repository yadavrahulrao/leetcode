# Detect Cycles in 2D Grid




class Solution(object):
    def containsCycle(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: bool
        """
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]

        def dfs(x, y, from_x, from_y, char, depth):
            if visited[x][y]:
                return depth >= 4  # Cycle detected if path length >= 4

            visited[x][y] = True

            for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                nx, ny = x + dx, y + dy

                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == char:
                    if nx == from_x and ny == from_y:
                        continue  # Skip immediate previous cell
                    if dfs(nx, ny, x, y, char, depth + 1):
                        return True

            return False

        for i in range(m):
            for j in range(n):
                if not visited[i][j]:
                    if dfs(i, j, -1, -1, grid[i][j], 1):
                        return True

        return False

