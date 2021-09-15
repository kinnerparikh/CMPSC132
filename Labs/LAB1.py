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
    if not isinstance(n, int) or (n < 1): #checking if n is a usable type
        return None

    retList = []
    for x in range(n, 0, -1): #loop from n to 0
        retList.append(x)
        retList.insert(0, x) #inserting x at the beginning of retList

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
    if not isinstance(txt, str) or len(txt) < 1: #checking if txt is a usable type
        return None

    if not txt.isalpha(): #check if txt is alpha only
        return False

    letterDict = {}
    for chr in txt.lower(): #iterate through txt
        if chr in letterDict: #checking if current letter exists in letterDict
            return False
        else:
            letterDict[chr] = 1 #adding chr to letterDict
    
    return (len(letterDict) == 26) #checking if letterDict is exactly 26 letters

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
    if not isinstance(aString, str) or len(aString) < 1: #checking if aString is a usable type
        return None

    retString = ''
    removedDict = {}
    for i in range(len(aString)): #iterate through aString indeces
        curr = aString[i]
        if not curr.isalpha() and curr != ' ': #checking if curr is not a letter and not a space
            if curr in removedDict:
                removedDict[curr] += 1 #increment the curr value in Dict
            else:
                removedDict[curr] = 1 #set the curr value in Dict
            curr = ' '
        retString += curr   

    return (retString, removedDict)
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()