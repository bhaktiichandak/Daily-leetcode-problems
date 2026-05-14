class Solution:
    def isGood(self, nums: List[int]) -> bool:
        
        mx = max(nums)
        ln = len(nums)

        if mx != (ln - 1):
            return False

        seen = set()
        cnt = 0
        for num in nums:
            if num > mx:
                return False
            if num == mx:
                cnt += 1
            else:
                if num in seen:
                    return False
                seen.add(num)
        
        return cnt == 2