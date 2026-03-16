class Solution:
    def getBiggestThree(self, grid):
        m, n = len(grid), len(grid[0])
        res = set()

        for r in range(m):
            for c in range(n):
                res.add(grid[r][c])  # k = 0 case

                k = 1
                while True:
                    if r-k < 0 or r+k >= m or c-k < 0 or c+k >= n:
                        break

                    total = 0

                    # top -> right
                    x, y = r-k, c
                    for i in range(k):
                        total += grid[x+i][y+i]

                    # right -> bottom
                    x, y = r, c+k
                    for i in range(k):
                        total += grid[x+i][y-i]

                    # bottom -> left
                    x, y = r+k, c
                    for i in range(k):
                        total += grid[x-i][y-i]

                    # left -> top
                    x, y = r, c-k
                    for i in range(k):
                        total += grid[x-i][y+i]

                    res.add(total)
                    k += 1

        return sorted(res, reverse=True)[:3]