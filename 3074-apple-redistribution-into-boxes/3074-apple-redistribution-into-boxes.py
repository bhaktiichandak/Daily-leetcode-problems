class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total_apples = sum(apple)
        
        capacity.sort(reverse=True)
        
        current = 0
        boxes = 0
        
        for cap in capacity:
            current += cap
            boxes += 1
            if current >= total_apples:
                return boxes
