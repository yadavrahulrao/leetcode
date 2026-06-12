#171. Excel Sheet Column Number
class Solution(object):
    def titleToNumber(self, columnTitle):
        res = 0
        for i in columnTitle:
          val = ord(i) - ord('A') + 1
          res = res * 26 + val
        return res 
