class Solution:
    def countElements(self, nums: List[int]) -> int:
        x=min(nums)
        y=max(nums)
        count=0
        for i in nums:
            if x<i<y:
                count+=1
        return count
        