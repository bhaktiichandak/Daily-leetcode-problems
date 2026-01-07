class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 10**9 + 7
        self.max_prod = 0
        
        # Step 1: get total sum
        def totalSum(node):
            if not node:
                return 0
            return node.val + totalSum(node.left) + totalSum(node.right)
        
        total = totalSum(root)
        
        # Step 2: compute subtree sums & maximize product
        def dfs(node):
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            curr_sum = node.val + left + right
            
            # try splitting here
            self.max_prod = max(
                self.max_prod,
                curr_sum * (total - curr_sum)
            )
            
            return curr_sum
        
        dfs(root)
        return self.max_prod % MOD
