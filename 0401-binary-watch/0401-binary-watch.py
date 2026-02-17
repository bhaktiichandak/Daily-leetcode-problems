class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        result = []
        
        for hour in range(12):
            for minute in range(60):
                total_bits = bin(hour).count('1') + bin(minute).count('1')
                
                if total_bits == turnedOn:
                    # format minute with leading zero
                    result.append(f"{hour}:{minute:02d}")
        
        return result
