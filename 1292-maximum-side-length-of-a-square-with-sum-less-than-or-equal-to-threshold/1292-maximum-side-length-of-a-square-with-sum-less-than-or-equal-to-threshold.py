from typing import List

class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])
        # build prefix sum matrix
        pre = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            row_sum = 0
            for j in range(n):
                row_sum += mat[i][j]
                pre[i + 1][j + 1] = pre[i][j + 1] + row_sum

        def square_exists(k: int) -> bool:
            # check if any k x k square has sum <= threshold
            for i in range(k, m + 1):
                for j in range(k, n + 1):
                    s = (
                        pre[i][j]
                        - pre[i - k][j]
                        - pre[i][j - k]
                        + pre[i - k][j - k]
                    )
                    if s <= threshold:
                        return True
            return False

        ans = 0
        # grow side length while feasible
        for k in range(1, min(m, n) + 1):
            if square_exists(k):
                ans = k
            else:
                break
        return ans