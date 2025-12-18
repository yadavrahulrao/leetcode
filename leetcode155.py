#50. Pow(x, n)
class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Handle negative powers
        if n < 0:
            x = 1 / x
            n = -n
        
        result = 1.0
        current_product = x
        
        while n > 0:
            # If n is odd, multiply the current product to the result
            if n % 2 == 1:
                result *= current_product
            # Square the current product and halve n
            current_product *= current_product
            n //= 2
        
        return result
