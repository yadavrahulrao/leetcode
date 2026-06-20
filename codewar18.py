
#Make a spiral
def spiralize(size):
    grid = [[0] * size for _ in range(size)]

    # right, down, left, up
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    r, c = 0, 0
    d = 0

    def valid(nr, nc):
        if not (0 <= nr < size and 0 <= nc < size):
            return False

        if grid[nr][nc] == 1:
            return False

        # Count neighbouring 1s
        neighbours = 0
        for dr, dc in dirs:
            rr, cc = nr + dr, nc + dc
            if 0 <= rr < size and 0 <= cc < size:
                if grid[rr][cc] == 1:
                    neighbours += 1

        # A new cell should only connect to the previous cell
        return neighbours <= 1

    while True:
        grid[r][c] = 1

        nr = r + dirs[d][0]
        nc = c + dirs[d][1]

        if valid(nr, nc):
            r, c = nr, nc
            continue

        d = (d + 1) % 4

        nr = r + dirs[d][0]
        nc = c + dirs[d][1]

        if valid(nr, nc):
            r, c = nr, nc
        else:
            break

    return grid