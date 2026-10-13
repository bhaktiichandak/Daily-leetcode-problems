class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        res , n = 0 , len(mat)
        for i in range(len(mat)):
            res += mat[i][i]
            res += mat[i][len(mat)-1-i]
        return res - (mat[n//2][n//2] if n % 2 else 0)