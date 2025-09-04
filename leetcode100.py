#118. Pascal's Triangle

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0 :
          return []

        tri = [[1]]

        for i in range(1,numRows):
          prev = tri[i-1]
          curr = [1]

          for j in range(1,i):
            curr.append(prev[j-1]+prev[j])
        
          curr.append(1)

          tri.append(curr)
        return tri
