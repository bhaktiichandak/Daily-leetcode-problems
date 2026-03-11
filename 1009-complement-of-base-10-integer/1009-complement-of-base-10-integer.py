class Solution:
    def bitwiseComplement(self, n: int) -> int:
        
        if n == 0:
            return 1
        
        # decimal → binary
        binary = ""
        temp = n
        
        while temp > 0:
            remainder = temp % 2
            binary = str(remainder) + binary
            temp = temp // 2
        
        # complement
        complement = ""
        for bit in binary:
            if bit == "0":
                complement += "1"
            else:
                complement += "0"
        
        # binary → decimal
        decimal = 0
        for bit in complement:
            decimal = decimal * 2 + int(bit)
        
        return decimal