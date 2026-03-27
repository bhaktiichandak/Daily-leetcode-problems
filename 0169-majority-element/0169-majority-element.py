class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        el = 0
        n = len(nums)
        cnt = 0
        for num in nums:
            if cnt == 0 :
                cnt = 1
                el = num
            elif el == num:
                cnt += 1
            else:
                cnt -= 1
        cnt1 = nums.count(el)
        if cnt1 > (n//2):
            return el
        return -1