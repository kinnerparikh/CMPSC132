# LAB3
# Due Date: 10/01/2021, 11:59PM
# REMINDERS: 
#        The work in this assignment must be your own original work and must be completed alone.
#        All functions should NOT contain any for/while loops or global variables. Use recursion, otherwise no credit will be given

def get_count(aList, item):
    '''
        >>> get_count([1,4,3.5,'1',3.5, 9, 1, 4, 2], 1)
        2
        >>> get_count([1,4,3.5,'1',3.5, 9, 4, 2], 3.5)  
        2
        >>> get_count([1,4,3.5,'1',3.5, 9, 4, 2], 9)   
        1
        >>> get_count([1,4,3.5,'1',3.5, 9, 4, 2], 'a') 
        0
    '''
    if len(aList) == 0: #base case of empty list
        return 0
    if aList[0] == item: #checking for instance of item
        return 1 + get_count(aList[1:], item) #adding one to the count
    return get_count(aList[1:], item)


#Used this resource for this problem
#https://stackoverflow.com/questions/2022031/python-append-vs-operator-on-lists-why-do-these-give-different-results
def replace(numList, old, new):
    '''
        >>> input_list = [1, 7, 5.6, 3, 2, 4, 1, 9]
        >>> replace(input_list, 1, 99.9)
        [99.9, 7, 5.6, 3, 2, 4, 99.9, 9]
        >>> input_list
        [1, 7, 5.6, 3, 2, 4, 1, 9]
        >>> replace([1,7, 5.6, 3, 2, 4, 1, 9], 5.6, 777) 
        [1, 7, 777, 3, 2, 4, 1, 9]
        >>> replace([1,7, 5.6, 3, 2, 4, 1, 9], 8, 99)    
        [1, 7, 5.6, 3, 2, 4, 1, 9]
    '''
    if len(numList) == 0: #base case for empty list
        return numList
    if numList[0] == old: #checking for instance of old
        return [new] + replace(numList[1:], old, new) #replacing item and performing on rest of list
    return [numList[0]] + replace(numList[1:], old, new)

def flat(aList):
    '''
        >>> x = [3, [[5, 2]], 6, [4]]
        >>> flat(x)
        [3, 5, 2, 6, 4]
        >>> x
        [3, [[5, 2]], 6, [4]]
        >>> flat([1, 2, 3])
        [1, 2, 3]
        >>> flat([1, [], 3])
        [1, 3]
    '''
    if len(aList) == 0: #base case for empty list
        return aList
    if isinstance(aList[0], list): #checking if current instance is list
        return flat(aList[0]) + flat(aList[1:]) #flatten both the current list and the remaining list
    return [aList[0]] + flat(aList[1:]) 

def neighbor(n):
    """
        >>> neighbor(24680)
        24680
        >>> neighbor(2222466666678)
        24678
        >>> neighbor(0)
        0
        >>> neighbor(22224666666782)
        246782
        >>> neighbor(2222466666625)
        24625
    """
    if n == 0: #base case for n being 0
        return n
    if n % 10 == (n // 10) % 10: #checking if the 1s and 10s place are the same
        return neighbor(n//10) #moving past the current value
    return n % 10 + 10 * neighbor(n//10) #adding the current value to the next values

if __name__=='__main__':
    import doctest
    doctest.run_docstring_examples(get_count, globals(), name='HW1',verbose=True)