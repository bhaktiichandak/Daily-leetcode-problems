class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        
        # prefix for balance (X=+1, Y=-1)
        balance = [[0]*n for _ in range(m)]
        
        # prefix for count of X
        countX = [[0]*n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                
                val = 0
                if grid[i][j] == 'X':
                    val = 1
                elif grid[i][j] == 'Y':
                    val = -1
                
                x = 1 if grid[i][j] == 'X' else 0
                
                balance[i][j] = val
                countX[i][j] = x
                
                if i > 0:
                    balance[i][j] += balance[i-1][j]
                    countX[i][j] += countX[i-1][j]
                if j > 0:
                    balance[i][j] += balance[i][j-1]
                    countX[i][j] += countX[i][j-1]
                if i > 0 and j > 0:
                    balance[i][j] -= balance[i-1][j-1]
                    countX[i][j] -= countX[i-1][j-1]
        
        ans = 0
        
        for i in range(m):
            for j in range(n):
                if balance[i][j] == 0 and countX[i][j] > 0:
                    ans += 1
        
        return ans