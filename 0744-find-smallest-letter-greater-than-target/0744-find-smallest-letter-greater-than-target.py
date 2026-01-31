class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left, right = 0, len(letters) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if letters[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        # left is the index of the smallest letter > target
        return letters[left % len(letters)]
