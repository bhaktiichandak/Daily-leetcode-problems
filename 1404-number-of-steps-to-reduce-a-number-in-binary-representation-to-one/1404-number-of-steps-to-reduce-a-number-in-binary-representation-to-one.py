class Solution:
    def numSteps(self, s: str) -> int:
        steps = 0
        carry = 0
        
        # Traverse from right to left (skip first bit)
        for i in range(len(s) - 1, 0, -1):
            
            bit = int(s[i])
            
            if bit + carry == 1:
                # odd case
                steps += 2
                carry = 1
            else:
                # even case
                steps += 1
        
        return steps + carry