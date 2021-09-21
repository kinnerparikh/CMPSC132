def doubleDigits(n):
    if (n < 1): return 0
    return (n%10)*11 + 100*doubleDigits(n//10)

def canWin(n):
    if (n <= 0): return False
    if (n == 1): return True

    takeOne = not canWin(n - 1)
    takeTwo = not canWin(n - 2)
    takeThree = not canWin(n - 3)

    return takeOne or takeTwo or takeThree

print(doubleDigits(1234))