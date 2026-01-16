class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: list[int], vFences: list[int]) -> int:
        MOD = 10**9 + 7
        
        # Add boundary fences
        h = sorted(hFences + [1, m])
        v = sorted(vFences + [1, n])
        
        # All possible horizontal distances
        h_dist = set()
        for i in range(len(h)):
            for j in range(i + 1, len(h)):
                h_dist.add(h[j] - h[i])
        
        # Check vertical distances and track max square side
        max_side = 0
        for i in range(len(v)):
            for j in range(i + 1, len(v)):
                d = v[j] - v[i]
                if d in h_dist:
                    max_side = max(max_side, d)
        
        if max_side == 0:
            return -1
        
        return (max_side * max_side) % MOD
