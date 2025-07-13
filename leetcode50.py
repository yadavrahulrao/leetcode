# Count and Say



class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = "1"
        
        for _ in range(1, n):
            current = ""
            i = 0
            while i < len(result):
                count = 1
                # Count consecutive repeating characters
                while i + 1 < len(result) and result[i] == result[i + 1]:
                    i += 1
                    count += 1
                # Append count followed by the digit
                current += str(count) + result[i]
                i += 1
            result = current
        
        return result
