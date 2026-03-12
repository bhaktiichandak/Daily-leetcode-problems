from typing import List

class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        parent = list(range(n))
        
        def find(x):
            if parent[x] == x:
                return x
            parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return False
            parent[py] = px
            return True
        
        def can(x):
            for i in range(n):
                parent[i] = i
            
            upgrades_left = k
            edges_count = 0
            mandatory_count = 0
            actual_mandatory_in_input = 0
            
            # 1. Mandatory Edges
            for u, v, s, m in edges:
                if m == 1:
                    actual_mandatory_in_input += 1
                    if s < x:
                        return False
                    if union(u, v):
                        edges_count += 1
                        mandatory_count += 1
                    else:
                        # This edge is mandatory but forms a cycle!
                        return False 
            
            # A Spanning tree MUST have exactly n-1 edges. 
            # If mandatory edges already exceed n-1 or form a cycle, it's impossible.
            if mandatory_count > n - 1:
                return False

            # 2. Free Optional Edges
            for u, v, s, m in edges:
                if m == 0 and s >= x:
                    if union(u, v):
                        edges_count += 1
            
            # 3. Upgradeable Optional Edges
            for u, v, s, m in edges:
                if edges_count == n - 1: break
                if m == 0 and s < x and s * 2 >= x:
                    if union(u, v):
                        if upgrades_left > 0:
                            upgrades_left -= 1
                            edges_count += 1
                        else:
                            # We need this edge to connect the graph, but no upgrades left
                            pass 
            
            return edges_count == n - 1

        # Binary Search
        max_s = 0
        for _, _, s, _ in edges:
            if s > max_s: max_s = s
            
        lo, hi = 0, max_s * 2
        ans = -1
        
        while lo <= hi:
            mid = (lo + hi) // 2
            if can(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        
        return ans