#2245. Maximum Trailing Zeros in a Cornered Path


class Solution:
    def maxTrailingZeros(self, grid):
        m, n = len(grid), len(grid[0])

        # Prefix sums for factors of 2 and 5
        row2 = [[0] * (n + 1) for _ in range(m)]
        row5 = [[0] * (n + 1) for _ in range(m)]
        col2 = [[0] * n for _ in range(m + 1)]
        col5 = [[0] * n for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                x = grid[i][j]

                c2 = c5 = 0

                while x % 2 == 0:
                    c2 += 1
                    x //= 2

                while x % 5 == 0:
                    c5 += 1
                    x //= 5

                row2[i][j + 1] = row2[i][j] + c2
                row5[i][j + 1] = row5[i][j] + c5

                col2[i + 1][j] = col2[i][j] + c2
                col5[i + 1][j] = col5[i][j] + c5

        ans = 0

        for i in range(m):
            for j in range(n):

                # Left + Up
                twos = row2[i][j + 1] + col2[i][j]
                fives = row5[i][j + 1] + col5[i][j]
                ans = max(ans, min(twos, fives))

                # Right + Up
                twos = row2[i][n] - row2[i][j] + col2[i][j]
                fives = row5[i][n] - row5[i][j] + col5[i][j]
                ans = max(ans, min(twos, fives))

                # Left + Down
                twos = row2[i][j + 1] + col2[m][j] - col2[i + 1][j]
                fives = row5[i][j + 1] + col5[m][j] - col5[i + 1][j]
                ans = max(ans, min(twos, fives))

                # Right + Down
                twos = (row2[i][n] - row2[i][j]) + \
                       (col2[m][j] - col2[i + 1][j])
                fives = (row5[i][n] - row5[i][j]) + \
                        (col5[m][j] - col5[i + 1][j])
                ans = max(ans, min(twos, fives))

        return ans
