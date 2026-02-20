class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        count = 0
        start = 0
        substrings = []
        
        for i in range(len(s)):
            if s[i] == '1':
                count += 1
            else:
                count -= 1
            
            # when balance becomes 0 → found a special substring
            if count == 0:
                # recursively solve inside part
                inside = self.makeLargestSpecial(s[start+1:i])
                substrings.append("1" + inside + "0")
                start = i + 1
        
        # sort in descending order
        substrings.sort(reverse=True)
        
        return "".join(substrings)