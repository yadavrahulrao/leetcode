#821. Shortest Distance to a Character

def shortestToChar(s, c):
    positions = [i for i, ch in enumerate(s) if ch == c]

    return [
        min(abs(i - p) for p in positions)
        for i in range(len(s))
    ]
