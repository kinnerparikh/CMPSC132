def canWin(n):
    if (n <= 0): return False
    if (n == 1): return True

    takeOne = not canWin(n - 1)
    takeTwo = not canWin(n - 2)
    takeThree = not canWin(n - 3)

    return takeOne or takeTwo or takeThree

print(canWin(5))