# Lab #1
# Due Date: 09/03/2021, 11:59PM
# REMINDER: The work in this assignment must be your own original work and must be completed alone.


def joinList(n):
    '''
        >>> joinList(5)
        [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]
        >>> joinList(1)
        [1, 1]
        >>> joinList(-3) is None
        True

    '''
    # - YOUR CODE STARTS HERE -
    #pass
    if not isinstance(n, int) or (n < 1): 
        return None

    retList = []
    for x in range(n, 0, -1):
        retList.append(x)
        retList.insert(0, x)

    return retList


def isValid(txt):
    '''
        >>> isValid('qwertyuiopASDFGHJKLzxcvbnm')
        True
        >>> isValid('hello there, fall is here!')
        False
        >>> isValid('123456yh')
        False
        >>> isValid('POIUYTqwerASDFGHlkjZXCVBMn')
        True
        >>> isValid('POIUYTqwerASDFGHlkjZXCVBnn')
        False
        >>> isValid('12aaaaaaaaaaa6543212345678')
        False
        >>> isValid([1]*26) is None
        True
    '''
    # - YOUR CODE STARTS HERE -
    # pass
    if not isinstance(txt, str) or len(txt) < 1: 
        return None

    letters = {}
    if (txt.isalpha()):
        letters = set(txt.lower())

    return (len(txt) == 26 and len(letters) == len(txt))


def removePunctuation(aString):
    '''
        >>> removePunctuation("Dots...................... many dots..X")
        ('Dots                       many dots  X', {'.': 24})
        
        >>> data = removePunctuation("I like chocolate cake!!(!! It's the best flavor..;.$ for real")
        >>> data[0]
        'I like chocolate cake      It s the best flavor      for real'
        >>> data[1]
        {'!': 4, '(': 1, "'": 1, '.': 3, ';': 1, '$': 1}
        
    '''
    # - YOUR CODE STARTS HERE -
    #pass
    if not isinstance(aString, str) or len(aString) < 1:
        return None

    removedList = {}
    for i in range(len(aString)):
        curr = aString[i]
        if not curr.isalpha:
            if curr in removedList:
                removedList[curr] += 1
            else:
                removedList[curr] = 1
            aString[i] = ' '
    
    retDict = [aString, removedList]
    return retDict

if __name__ == "__main__":
    import doctest
    doctest.testmod()