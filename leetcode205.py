#119. Pascal's Triangle II
class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        row = [1]
        for i in range(1,rowIndex+1):
          nxt = row[-1] * (rowIndex - i +1 )// i
          row.append(nxt)
        return row