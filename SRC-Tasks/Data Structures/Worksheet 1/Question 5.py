# Program doesn’t mention needing this game to repeat, so coded as if this game only loops once.

grid = [["x" for _ in range(4)] for __ in range(6)]
grid[0][0] = "O"
print(grid)