from collections import defaultdict

class Solution:
    def minimumDistance(self, nums):
        pos = defaultdict(list)
        
        # store indices
        for i, x in enumerate(nums):
            pos[x].append(i)
        
        ans = float('inf')
        
        # process each value
        for indices in pos.values():
            if len(indices) < 3:
                continue
            
            # check consecutive triples
            for i in range(len(indices) - 2):
                dist = 2 * (indices[i+2] - indices[i])
                ans = min(ans, dist)
        
        return ans if ans != float('inf') else -1