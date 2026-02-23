class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        n = len(s)
        
        # Early pruning
        if n < k:
            return False
        
        if n - k + 1 < (1 << k):
            return False
        
        seen = set()
        
        for i in range(n - k + 1):
            seen.add(s[i:i+k])
            
            # Early stopping
            if len(seen) == (1 << k):
                return True
        
        return len(seen) == (1 << k)