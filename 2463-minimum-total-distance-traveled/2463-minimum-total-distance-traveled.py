from math import inf

class Solution:
    def minimumTotalDistance(self, robot, factory):
        robot.sort()
        factory.sort()
        
        # expand factories
        slots = []
        for pos, limit in factory:
            slots.extend([pos] * limit)
        
        n, m = len(robot), len(slots)
        
        # dp[i][j] = first i robots, first j slots
        dp = [[inf] * (m + 1) for _ in range(n + 1)]
        
        # base case
        for j in range(m + 1):
            dp[0][j] = 0
        
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                # skip slot
                dp[i][j] = dp[i][j-1]
                
                # use slot
                cost = abs(robot[i-1] - slots[j-1])
                dp[i][j] = min(dp[i][j], dp[i-1][j-1] + cost)
        
        return dp[n][m]