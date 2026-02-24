class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node, curr):
            if not node:
                return 0
            
            # Build binary number
            curr = (curr << 1) | node.val
            
            # If leaf → return the number
            if not node.left and not node.right:
                return curr
            
            # Otherwise sum left + right
            return dfs(node.left, curr) + dfs(node.right, curr)
        
        return dfs(root, 0)