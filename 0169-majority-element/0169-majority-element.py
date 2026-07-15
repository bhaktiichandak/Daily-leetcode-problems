from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = Counter(nums)

        for key, value in freq.items():
            if value > len(nums) // 2:
                return key

        return -1