#29. Divide Two Integers



class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # Handle overflow case
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        # Determine the sign of the result
        negative = (dividend < 0) != (divisor < 0)

        # Convert both numbers to positive
        dividend_abs = abs(dividend)
        divisor_abs = abs(divisor)

        result = 0

        # Bit manipulation division
        while dividend_abs >= divisor_abs:
            temp = divisor_abs
            multiple = 1

            # Find the largest multiple of divisor that fits into dividend
            while dividend_abs >= (temp << 1):
                temp <<= 1
                multiple <<= 1

            # Subtract the found multiple from dividend
            dividend_abs -= temp
            result += multiple

        # Apply the sign
        if negative:
            result = -result

        # Clamp to 32-bit signed integer range
        return max(INT_MIN, min(INT_MAX, result))
