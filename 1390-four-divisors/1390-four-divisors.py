class Solution:
    def sumFourDivisors(self, nums):
        total = 0

        for n in nums:
            divisors = {1, n}
            i = 2

            while i * i <= n and len(divisors) <= 4:
                if n % i == 0:
                    divisors.add(i)
                    divisors.add(n // i)
                i += 1

            if len(divisors) == 4:
                total += sum(divisors)

        return total
