class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        
        num_seen = False
        dot_seen = False
        e_seen = False
        num_after_e = True
        
        for i, ch in enumerate(s):
            
            if ch.isdigit():
                num_seen = True
                num_after_e = True
            
            elif ch in ['+', '-']:
                # only valid at start OR right after e
                if i > 0 and s[i-1] not in ['e', 'E']:
                    return False
            
            elif ch == '.':
                # dot only once and before e
                if dot_seen or e_seen:
                    return False
                dot_seen = True
            
            elif ch in ['e', 'E']:
                # only once and must have number before
                if e_seen or not num_seen:
                    return False
                e_seen = True
                num_after_e = False
            
            else:
                return False
        
        return num_seen and num_after_e