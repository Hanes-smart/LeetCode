import math

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        num = int(dividend/divisor)
        if num > pow(2,31)-1:
            return pow(2,31)-1
        if num < -pow(2,31):
            return -pow(2,31)
        
        return num
        