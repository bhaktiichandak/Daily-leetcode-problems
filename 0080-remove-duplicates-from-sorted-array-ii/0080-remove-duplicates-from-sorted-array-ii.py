class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n <= 2:
            return n
        
        write = 2  # first two elements always allowed
        
        for i in range(2, n):
            if nums[i] != nums[write - 2]:
                nums[write] = nums[i]
                write += 1
        
        return write