from collections import defaultdict

class Solution:
    def minimumDistance(self, nums):
        last = defaultdict(list)
        ans = float('inf')
        
        for i, x in enumerate(nums):
            last[x].append(i)
            
            # keep only last 3 indices
            if len(last[x]) > 3:
                last[x].pop(0)
            
            # if we have 3 indices → compute
            if len(last[x]) == 3:
                i1, i2, i3 = last[x]
                ans = min(ans, 2 * (i3 - i1))
        
        return ans if ans != float('inf') else -1