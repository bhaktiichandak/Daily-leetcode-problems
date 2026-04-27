class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])

        ans = []

        for c in range(n):
            row = []
            for r in range(m):
                row.append(matrix[r][c])
            ans.append(row)

        return ans

