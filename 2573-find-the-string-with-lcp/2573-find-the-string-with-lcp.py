from typing import List

class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)
        
        # ---------- Step 1: Basic validation ----------
        for i in range(n):
            if lcp[i][i] != n - i:
                return ""
            for j in range(n):
                if lcp[i][j] != lcp[j][i]:
                    return ""
        
        # ---------- Step 2: Build string ----------
        word = [''] * n
        curr_char = ord('a')
        
        for i in range(n):
            if word[i] == '':
                if curr_char > ord('z'):
                    return ""
                
                word[i] = chr(curr_char)
                
                for j in range(i + 1, n):
                    if lcp[i][j] > 0:
                        word[j] = word[i]
                
                curr_char += 1
        
        word = ''.join(word)
        
        # ---------- Step 3: Validate by recomputing LCP ----------
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if word[i] == word[j]:
                    dp[i][j] = dp[i + 1][j + 1] + 1
                else:
                    dp[i][j] = 0
        
        # compare with given lcp
        for i in range(n):
            for j in range(n):
                if dp[i][j] != lcp[i][j]:
                    return ""
        
        return word