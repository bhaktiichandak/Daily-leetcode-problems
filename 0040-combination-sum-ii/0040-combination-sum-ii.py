class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()
        res = []
        
        def backtrack(start, path, target):
            if target == 0:
                res.append(path[:])
                return
            
            if target < 0:
                return
            
            for i in range(start, len(candidates)):
                
                # skip duplicates
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                
                # optimization
                if candidates[i] > target:
                    break
                
                path.append(candidates[i])
                backtrack(i + 1, path, target - candidates[i])  # move forward (no reuse)
                path.pop()
        
        backtrack(0, [], target)
        return res