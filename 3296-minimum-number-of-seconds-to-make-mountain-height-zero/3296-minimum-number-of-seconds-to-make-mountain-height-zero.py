from typing import List
import math

class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:

        def canFinish(time):
            total = 0
            for t in workerTimes:
                x = int((math.sqrt(1 + 8 * time / t) - 1) // 2)
                total += x
                if total >= mountainHeight:
                    return True
            return False

        left, right = 0, min(workerTimes) * mountainHeight * (mountainHeight + 1) // 2

        while left < right:
            mid = (left + right) // 2
            if canFinish(mid):
                right = mid
            else:
                left = mid + 1

        return left