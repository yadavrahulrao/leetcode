#Given two binary strings a and b, return their sum as a binary string.

class Solution:
    def addBinary(self, a, b):
        # Convert the binary strings to integers
        a_int = int(a, 2)
        b_int = int(b, 2)

        # Add the two integers
        sum_int = a_int + b_int

        # Convert the sum back to a binary string and remove the "0b" prefix
        return bin(sum_int)[2:]

# Example usage:
def _driver():
    # Example input
    param_1 = "11"
    param_2 = "1"
    
    # Call the method from Solution class
    ret = Solution().addBinary(param_1, param_2)
    print(ret)  # Output: "100"

_driver()
