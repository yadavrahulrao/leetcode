#221. Maximal Square


class Solution:
    def maximalSquare(self, matrix):
        m, n = len(matrix), len(matrix[0])

        ans = 0

        for r in range(m):
            for c in range(n):

                if matrix[r][c] == '0':
                    continue

                if r == 0 or c == 0:
                    matrix[r][c] = 1
                else:
                    matrix[r][c] = 1 + min(
                        matrix[r - 1][c],
                        matrix[r][c - 1],
                        matrix[r - 1][c - 1]
                    )

                ans = max(ans, matrix[r][c])

        return ans * ans