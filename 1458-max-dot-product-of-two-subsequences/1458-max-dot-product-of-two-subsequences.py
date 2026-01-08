class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        NEG_INF = -10**18
        
        dp = [[NEG_INF] * (m + 1) for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                prod = nums1[i - 1] * nums2[j - 1]
                
                take = prod + max(0, dp[i - 1][j - 1])
                skip1 = dp[i - 1][j]
                skip2 = dp[i][j - 1]
                
                dp[i][j] = max(take, skip1, skip2)
        
        return dp[n][m]
