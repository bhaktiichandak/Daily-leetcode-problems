class Solution:
    def dailyTemperatures(self, temperatures):
        n = len(temperatures)

        res = [0] * n
        stack = []  # (index, temperature)

        for i, t in enumerate(temperatures):

            while stack and t > stack[-1][1]:
                prev_idx, prev_temp = stack.pop()
                res[prev_idx] = i - prev_idx

            stack.append((i, t))

        return res