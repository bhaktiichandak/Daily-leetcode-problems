class Solution:
    def findGCD(self, nums: List[int]) -> int:
        from math import gcd
        mn = min(nums)
        mx = max(nums)
        return gcd(mn, mx)
