class Solution:
    def dfs(self, grid, x, y, count):
        if 0 <= x < len(grid) and 0 <= y < len(grid[x]) and grid[x][y] == '1':
            grid[x][y] = count
            self.dfs(grid, x - 1, y, count)
            self.dfs(grid, x + 1, y, count)
            self.dfs(grid, x, y - 1, count)
            self.dfs(grid, x, y + 1, count)

    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if grid[x][y] == "1":
                    count += 1
                    self.dfs(grid, x, y, count)
        return count


class Solution:
    def bfs(self, grid, x, y, count):
        queue = deque()
        queue.append((x, y))
        while queue:
            x, y = queue.popleft()
            if 0 <= x < len(grid) and 0 <= y < len(grid[x]) and grid[x][y] == '1':
                grid[x][y] = count
                for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                    queue.append((x + dx, y + dy))



    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if grid[x][y] == "1":
                    count += 1
                    self.bfs(grid, x, y, count)
        return count
