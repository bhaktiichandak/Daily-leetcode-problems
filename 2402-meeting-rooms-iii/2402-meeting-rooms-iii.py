import heapq
from typing import List

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        
        available = list(range(n))
        heapq.heapify(available)
        
        busy = []  # (endTime, room)
        count = [0] * n
        
        for start, end in meetings:
            duration = end - start
            
            # Free rooms that have finished
            while busy and busy[0][0] <= start:
                _, room = heapq.heappop(busy)
                heapq.heappush(available, room)
            
            if available:
                room = heapq.heappop(available)
                heapq.heappush(busy, (end, room))
            else:
                endTime, room = heapq.heappop(busy)
                heapq.heappush(busy, (endTime + duration, room))
            
            count[room] += 1
        
        return count.index(max(count))
