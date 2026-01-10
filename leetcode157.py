#37. Sudoku Solver


class Solution:
    def solveSudoku(self, board):
        # Track used numbers
        rows = [[False] * 10 for _ in range(9)]
        cols = [[False] * 10 for _ in range(9)]
        boxes = [[False] * 10 for _ in range(9)]

        # Initialize trackers
        for r in range(9):
            for c in range(9):
                if board[r][c] != '.':
                    d = int(board[r][c])
                    rows[r][d] = True
                    cols[c][d] = True
                    boxes[(r // 3) * 3 + (c // 3)][d] = True

        def backtrack(r, c):
            # Move to next row
            if c == 9:
                return backtrack(r + 1, 0)
            # Finished entire board
            if r == 9:
                return True
            # Skip filled cells
            if board[r][c] != '.':
                return backtrack(r, c + 1)

            box_id = (r // 3) * 3 + (c // 3)
            for d in range(1, 10):
                if not rows[r][d] and not cols[c][d] and not boxes[box_id][d]:
                    # Place digit
                    board[r][c] = str(d)
                    rows[r][d] = cols[c][d] = boxes[box_id][d] = True

                    if backtrack(r, c + 1):
                        return True

                    # Undo
                    board[r][c] = '.'
                    rows[r][d] = cols[c][d] = boxes[box_id][d] = False

            return False

        backtrack(0, 0)
