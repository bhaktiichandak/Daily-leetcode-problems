class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashMap ={ ")" : "(" , "]" : "[" , "}" : "{" }
        for ch in s:
            if ch in hashMap:
                if stack and stack[-1] == hashMap[ch]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)
        return len(stack) == 0