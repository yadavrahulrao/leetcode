#73. Set Matrix Zeroes
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        r = len(matrix)
        c = len(matrix[0])
        lst = []
        for i in range(r):
          for j in range(c):
            if matrix[i][j] == 0 :
              lst.append((i,j))
        for k, l in lst:
          matrix[k] = [0] *c
          for b in range(r):
            matrix[b][l] = 0
        return matrix
s = Solution()
print(s.setZeroes([[1,1,1],[1,0,1],[1,1,1]]))