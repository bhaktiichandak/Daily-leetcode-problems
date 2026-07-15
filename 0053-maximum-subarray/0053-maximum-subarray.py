class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        current_sum = 0
        for i in range(len(nums)):
            current_sum = max(nums[i] ,current_sum + nums[i])
            max_sum = max(current_sum , max_sum)
        return max_sum
