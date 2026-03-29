from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(list)
        
        for s in strs:
            key = ''.join(sorted(s))  # sorted string as key
            mp[key].append(s)
        
        return list(mp.values())