class Solution:
    def binaryGap(self, n: int) -> int:
        last = -1
        maxGap = 0
        position = 0
        
        while n > 0:
            if n & 1:  # if current bit is 1
                if last != -1:
                    maxGap = max(maxGap, position - last)
                last = position
            n >>= 1
            position += 1
        
        return maxGap