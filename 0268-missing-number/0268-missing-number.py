class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        length=len(nums)
        expectedsum=(length*(length+1))//2
        actualsum=sum(nums)
        return expectedsum-actualsum