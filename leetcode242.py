#289. Game of Life



class Solution:
    def gameOfLife(self, board):
        rows, cols = len(board), len(board[0])

        directions = [
            (-1,-1), (-1,0), (-1,1),
            (0,-1),         (0,1),
            (1,-1), (1,0), (1,1)
        ]

        for r in range(rows):
            for c in range(cols):

                live = 0

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < rows and 0 <= nc < cols:
                        live += board[nr][nc] & 1

                if board[r][c] == 1:
                    if live == 2 or live == 3:
                        board[r][c] |= 2
                else:
                    if live == 3:
                        board[r][c] |= 2

        for r in range(rows):
            for c in range(cols):
                board[r][c] >>= 1