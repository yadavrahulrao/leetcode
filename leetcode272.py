#766. Toeplitz Matrix

class Solution(object):
    def isToeplitzMatrix(self, matrix):
        
    
        rows, cols = len(matrix), len(matrix[0])

        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] != matrix[i - 1][j - 1]:
                    return False

        return True


obj = Solution()
print(obj.isToeplitzMatrix([[1,2,3,4],[5,1,2,3],[9,5,1,2]]))
        
        