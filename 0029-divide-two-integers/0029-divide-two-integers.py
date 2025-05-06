class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MAX = pow(2,31)-1
        MIN = -pow(2,31)

        a = abs(dividend)
        b = abs(divisor)
        output = 0

        negative = (dividend >=0 and divisor <0) or (dividend<0 and divisor >=0)

        while a >= b:  
            counter = 1
            decrement = b
            
            while a >= decrement:
                a -= decrement

                output +=counter 
                counter += counter
                decrement += decrement

        output = output if not negative else -output

        return min(max(MIN,output),MAX)
     