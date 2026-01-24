"Divide without using * / %. Clamp result to 32-bit range."

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Determine the sign of the result
        negative = (dividend < 0) ^ (divisor < 0)

        # Work with absolute values
        dividend, divisor = abs(dividend), abs(divisor)

        quotient = 0
        # Subtract divisor from dividend until dividend < divisor
        while dividend >= divisor:
            temp, multiple = divisor, 1
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            dividend -= temp
            quotient += multiple

        if negative:
            quotient = -quotient

        # Clamp to 32-bit signed integer range
        return max(-2**31, min(quotient, 2**31 - 1))
