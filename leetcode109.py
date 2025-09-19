#17. Letter Combinations of a Phone Number
from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Map of digits to corresponding letters
        phone_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        
        # Result list to collect combinations
        res = []
        
        # Edge case: if input is empty
        if not digits:
            return res
        
        # Helper function for backtracking
        def backtrack(index: int, path: str):
            # Base case: if path length equals digits length, we found a combination
            if index == len(digits):
                res.append(path)
                return
            
            # Get the letters that the current digit maps to
            possible_letters = phone_map[digits[index]]
            for letter in possible_letters:
                # Explore further by adding one letter to the path
                backtrack(index + 1, path + letter)
        
        # Start the backtracking process
        backtrack(0, "")
        return res
