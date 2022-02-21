# HW1
# Due Date: 09/10/2021, 11:59PM
# REMINDER: The work in this assignment must be your own original work and must be completed alone.



def rectangle(perimeter,area):
    """
        >>> rectangle(14, 10)
        5
        >>> rectangle(12, 5)
        5
        >>> rectangle(25, 25)
        False
        >>> rectangle(50, 100)
        20
        >>> rectangle(11, 5)
        False
        >>> rectangle(11, 4)
        False
    """
    #- YOUR CODE STARTS HERE
    #pass
    if not perimeter % 2 == 0: #perimeters cannot be odd
        return False

    longSide = (perimeter + abs(perimeter**2 - 16*area)**0.5)/4 #logic for finding one side of the rectangle
    shortSide = area / longSide

    if longSide.is_integer() and shortSide.is_integer(): #checking if both side lengths are integers
        return round(longSide)
    else: 
        return False



def frequency(aString):
    """
        >>> frequency('mama')
        ('consonant', {'m': 2, 'a': 2})
        >>> answer = frequency('We ARE Penn State!!!')
        >>> answer[0]
        'vowel'
        >>> answer[1]
        {'w': 1, 'e': 4, 'a': 2, 'r': 1, 'p': 1, 'n': 2, 's': 1, 't': 2}
        >>> frequency('One who IS being Trained')
        ('consonant', {'o': 2, 'n': 3, 'e': 3, 'w': 1, 'h': 1, 'i': 3, 's': 1, 'b': 1, 'g': 1, 't': 1, 'r': 1, 'a': 1, 'd': 1})
    """
    #- YOUR CODE STARTS HERE
    letterDict = {}
    for letter in aString.lower(): #iterate through string
        if letter.isalpha():
            if letter in letterDict: #check if key already exists in the dictionary
                letterDict[letter] += 1
            else:
                letterDict[letter] = 1
    
    maxValue = 0
    maxLetter = ''
    for letter, value in letterDict.items(): #iterating through the dictionary items
        if value > maxValue: #checking if the number of occurances is greater than the previous greatest
            maxLetter = letter
            maxValue = value

    if maxLetter in 'aeiou': #check if the letter is a vowel
        return ('vowel', letterDict)
    else:
        return ('consonant', letterDict)

    

# THIS IMPLEMENTATION DOES NOT WORK CORRECTLY 
def successors(file):
    """
        >>> expected = {'.': ['We', 'Maybe'], 'We': ['came'], 'came': ['to'], 'to': ['learn', 'have', 'make'], 'learn': [',', 'how'], ',': ['eat'], 'eat': ['some'], 'some': ['pizza'], 'pizza': ['and', 'too'], 'and': ['to'], 'have': ['fun'], 'fun': ['.'], 'Maybe': ['to'], 'how': ['to'], 'make': ['pizza'], 'too': ['!']}
        >>> returnedDict = successors('items.txt')
        >>> expected == returnedDict
        True
        >>> returnedDict['.']
        ['We', 'Maybe']
        >>> returnedDict['to']
        ['learn', 'have', 'make']
        >>> returnedDict['fun']
        ['.']
        >>> returnedDict[',']
        ['eat']
    """

    with open(file) as f: 
        contents = f.read()

    #- YOUR CODE STARTS HERE
    
    uncleanedList = contents.replace('\n', ' ').split(' ') #remove the \n and split
    cleanedList = []
    for index in range(0, len(uncleanedList)): #iterate through the list
        curr = uncleanedList[index]
        if not curr.isalnum(): #checking if the current value is alphanumeric
            currList = list(curr) #splitting into individual characters
            for i in range(len(currList) - 1, 0, -1): #iterating through the list backwards
                if not currList[i].isalnum():
                    temp = currList[:i]       #inputting spaces into the list
                    temp.append(" ")
                    temp.append(currList[i])
                    temp.append(" ")
                    temp += currList[i + 1:]
                    currList = temp
                    i -= 1
            combinedList = ''
            for i in range(0, len(currList)): #combining list into 1 string
                combinedList += currList[i]
            cleanedList += combinedList.split(' ')
        else:
            cleanedList.append(curr)
        
        cleanedList = ' '.join(cleanedList).split() #cleaning up the list to clear empty values

    retDict = {'.': [cleanedList[0]]} #initializing dictionary

    for index in range(0, len(cleanedList) - 1): #iterating through cleanedList
        key = cleanedList[index]
        if key in retDict: 
            if cleanedList[index + 1] not in retDict[key]: #checking if the value already exists
                retDict[key].append(cleanedList[index + 1])
        else:
            retDict[key] = [cleanedList[index + 1]] #creating a new key value pair 
    
    return retDict


def getPosition(num, digit):
    """
        >>> getPosition(1495, 5)
        1
        >>> getPosition(1495, 1)
        4
        >>> getPosition(1495423, 4)
        3
        >>> getPosition(1495, 7)
        False
    """
    #- YOUR CODE STARTS HERE
    #pass
    currPos = 0
    while not num == 0: #looping till all digits are checked
        currPos += 1
        if num % 10 == digit: #checking if the last digit is equal to digit
            return currPos
        else:
            num = num // 10 #floor divide num by 10

    return False

def hailstone(n):
    """
        >>> hailstone(10)
        [10, 5, 16, 8, 4, 2, 1]
        >>> hailstone(1)
        [1]
        >>> hailstone(27)
        [27, 82, 41, 124, 62, 31, 94, 47, 142, 71, 214, 107, 322, 161, 484, 242, 121, 364, 182, 91, 274, 137, 412, 206, 103, 310, 155, 466, 233, 700, 350, 175, 526, 263, 790, 395, 1186, 593, 1780, 890, 445, 1336, 668, 334, 167, 502, 251, 754, 377, 1132, 566, 283, 850, 425, 1276, 638, 319, 958, 479, 1438, 719, 2158, 1079, 3238, 1619, 4858, 2429, 7288, 3644, 1822, 911, 2734, 1367, 4102, 2051, 6154, 3077, 9232, 4616, 2308, 1154, 577, 1732, 866, 433, 1300, 650, 325, 976, 488, 244, 122, 61, 184, 92, 46, 23, 70, 35, 106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1]
        >>> hailstone(7)
        [7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
        >>> hailstone(19)
        [19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
    """
    #- YOUR CODE STARTS HERE
    #pass
    retList = [n] #initialize list with n
    while not n == 1: #loop till n becomes 1
        if (n % 2 == 0): #even case
            n /= 2
        else: #odd case
            n = (3 * n) + 1
        retList.append(round(n)) #append n to the list
    
    return retList

def largeFactor(num):
    """
        >>> largeFactor(15)
        5
        >>> largeFactor(80)
        40
        >>> largeFactor(13)
        1
        >>> largeFactor(57)
        19
    """
    #- YOUR CODE STARTS HERE
    #pass
    for factor in range(2, round(num / 2) + 1): #iterating through first half of num
        if num % factor == 0: #checking if it is a factor
            return round(num/factor) #returning largest factor
    
    return 1 #default case

#  To run doctes per function, uncomment the next three lines
#  and replace the word rectangle for the function name you want to test

if __name__=='__main__':
    import doctest
    doctest.run_docstring_examples(successors, globals(), name='HW1',verbose=True)