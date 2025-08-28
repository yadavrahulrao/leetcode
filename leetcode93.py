# 12. Integer to Roman

class Solution:
    """
    A class to convert an integer to a Roman numeral.
    """
    def intToRoman(self, num: int) -> str:
        """
        Converts an integer to a Roman numeral string.

        Args:
            num: The integer to convert (1 <= num <= 3999).

        Returns:
            The Roman numeral representation as a string.
        """
        # A list of tuples containing Roman numeral values and symbols,
        # ordered from largest to smallest. This order is crucial for
        # the greedy algorithm to work correctly, especially for
        # subtractive forms like CM, CD, XC, XL, IX, and IV.
        value_symbols = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I")
        ]

        # An empty string to build the Roman numeral result.
        roman_numeral = ""

        # Iterate through the predefined values in descending order.
        for value, symbol in value_symbols:
            # Continue appending the symbol and subtracting its value
            # as long as the current number is greater than or equal to the value.
            while num >= value:
                roman_numeral += symbol
                num -= value

        return roman_numeral

# Example Usage:
# Create an instance of the Solution class
converter = Solution()

# Test with Example 1: 3749
num1 = 3749
result1 = converter.intToRoman(num1)
print(f"The Roman numeral for {num1} is: {result1}")
# Expected output: MMMDCCXLIX

# Test with Example 2: 58
num2 = 58
result2 = converter.intToRoman(num2)
print(f"The Roman numeral for {num2} is: {result2}")
# Expected output: LVIII

# Test with Example 3: 1994
num3 = 1994
result3 = converter.intToRoman(num3)
print(f"The Roman numeral for {num3} is: {result3}")
# Expected output: MCMXCIV
