#Lab #0
#Due Date: 08/28/2021, 11:59PM

# More information on pass statement: 
#    https://docs.python.org/3/reference/simple_stmts.html#the-pass-statement

def sumSquares(aList):
    """
        >>> sumSquares([1,5,-3,5.5,359,8,14,-25,1000])
        129171.25
        >>> sumSquares([1,5,-3,5,45.5,8.5,-5,500,6.7,-25])
        2187.39
        >>> sumSquares(['14',5,-3,5,9.0,8,14,7,'Hello'])
        390.0
        >>> sumSquares(5)
        >>> sumSquares('5') is None
        True
        >>> sumSquares(6.15)

    """
    # --- YOU CODE STARTS HERE
    if not isinstance(aList, list) or len(aList) == 0: #checking if input is a list or is empty
        return None

    finalSum = 0
    for item in aList:
        if isinstance(item, (float, int, complex)) and item > 5 and item < 500: #check if item in list is numerical and in bounds
            finalSum += item**2
    return finalSum

## Uncomment next 3 lines if not running doctest in the command line
if __name__ == "__main__":
    import doctest
    doctest.testmod()