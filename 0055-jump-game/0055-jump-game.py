from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        
        for i in range(len(nums)):
            # can't reach this index
            if i > max_reach:
                return False
            
            # update farthest reachable
            max_reach = max(max_reach, i + nums[i])
        
        return True