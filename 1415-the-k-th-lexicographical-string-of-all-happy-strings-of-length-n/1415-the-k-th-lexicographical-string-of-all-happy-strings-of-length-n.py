class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        res = []
        
        def dfs(curr):
            if len(curr) == n:
                res.append(curr)
                return
            
            for ch in ['a', 'b', 'c']:
                if not curr or curr[-1] != ch:
                    dfs(curr + ch)
        
        dfs("")
        
        if k <= len(res):
            return res[k-1]
        return ""
