class Solution:
    def check(self, nums: List[int]) -> bool:
        count = 0
        n = len(nums)

        for i in range(n):
            if nums[i] > nums[(i + 1) % n]: #used modulo so that after finishing the    array we go back to the first element rather than index bound 
                count += 1

        return count <= 1