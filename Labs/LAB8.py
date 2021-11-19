#Lab #8
#Due Date: 12/03/2021, 11:59PM 



def matrixCalculator(matrix1, matrix2, operation):
    '''
        >>> matrixCalculator([[2, 1], [-3, 6]], [[1, 3], [4, -1]],'sub')
        [[1, -2], [-7, 7]]
        >>> matrixCalculator([[3, 1], [2, 7]], [[4, 2], [5, 7]],'add')
        [[7, 3], [7, 14]]
        >>> matrixCalculator([[8, 2, -6, 2], [1, 5, 2, 24.5], [34, 4, 4, 2], [5, -98, 1.5, 4]], [[1, 7, 9, 55], [9.5, 45.5, 5, -9], [1, 5, 6, 67], [8, 4, 1, 7]],'add')
        [[9, 9, 3, 57], [10.5, 50.5, 7, 15.5], [35, 9, 10, 69], [13, -94, 2.5, 11]]
        >>> matrixCalculator([[8, 9, 10], [7.5, 2, -8], [1, 1, 1]], [[4, 2, 3], [43, 2, 32], [-2, 5.5, 3]],'sub')
        [[4, 7, 7], [-35.5, 0, -40], [3, -4.5, -2]]
    '''
    # non-list comprehension solution
    # --------------------------------------
    # temp = matrix1
    # for i in range(len(matrix1)):
    #     for j in range(len(matrix1[0])):
    #         if operation == 'add':
    #             temp[i][j] += matrix2[i][j]
    #         else:
    #             temp[i][j] -= matrix2[i][j]
    if operation == 'add': return [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]
    elif operation == 'sub': return [[matrix1[i][j] - matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]
    




def mulDigits(num, fn):
    '''
        >>> isTwo = lambda num: num == 2
        >>> mulDigits(5724892472, isTwo)
        8
        >>> def divByFour(num):
        ...     return not num%4
        ...
        >>> mulDigits(5724892472, divByFour)
        128
        >>> mulDigits(155794, isTwo)
        1
        >>> mulDigits(67945125482222152, isTwo)
        64
        >>> mulDigits(679451254828822152, divByFour)
        8192
    '''
    # YOUR CODE STARTS HERE
    pass




def getCount(x):
    '''
        >>> getCount(6)(62156)
        2
        >>> digit = getCount(7)
        >>> digit(9457845778457077076)
        7
        >>> digit(-945784578457077076)
        6
        >>> getCount(6)(-65062156)
        3
    '''
    # YOUR CODE STARTS HERE
    pass





def itemize(seq):
    '''
        >>> gen = itemize('We ARE!')
        >>> next(gen)
        (0, 'W')
        >>> next(gen)
        (1, 'e')
        >>> next(gen)
        (2, ' ')
        >>> next(gen)
        (3, 'A')
        >>> next(gen)
        (4, 'R')
        >>> next(gen)
        (5, 'E')
        >>> next(gen)
        (6, '!')
        >>> next(gen)
        Traceback (most recent call last):
        ...
        StopIteration
        >>> list(itemize([78, 76, 54, 34.8, 'hi']))
        [(0, 78), (1, 76), (2, 54), (3, 34.8), (4, 'hi')]
    '''
    # YOUR CODE STARTS HERE
    pass


def frange(*args):
    '''
        >>> list(frange(7.5))
        [0, 1, 2, 3, 4, 5, 6, 7]
        >>> seq = frange(0,7, 0.1)
        >>> type(seq)
        <class 'generator'>
        >>> list(seq)
        [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 3.0, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8, 3.9, 4.0, 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 4.8, 4.9, 5.0, 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 5.7, 5.8, 5.9, 6.0, 6.1, 6.2, 6.3, 6.4, 6.5, 6.6, 6.7, 6.8, 6.9, 7.0]
        >>> list(seq)
        []
        >>> list(frange(0,7, 0.75))
        [0, 0.75, 1.5, 2.25, 3.0, 3.75, 4.5, 5.25, 6.0, 6.75]
        >>> list(frange(0,7.75, 0.75))
        [0, 0.75, 1.5, 2.25, 3.0, 3.75, 4.5, 5.25, 6.0, 6.75, 7.5]
        >>> list(frange(0,7.75, -0.5))
        []
        >>> list(frange(7.75,0, -0.5))
        [7.75, 7.25, 6.75, 6.25, 5.75, 5.25, 4.75, 4.25, 3.75, 3.25, 2.75, 2.25, 1.75, 1.25, 0.75, 0.25]
    '''
    start, step = 0, 1

    if len(args) == 1:
        stop = args[0]
    elif len(args) == 2:
        start, stop = args
    elif len(args) == 3:
        start = args[0]
        stop = args[1]
        step = args[2]
    else:
        raise TypeError(f'frange expected at most 3 arguments, got {len(args)}')
    
    # YOUR CODE STARTS HERE
    pass



def genFib(fn):
    '''
        >>> evens = genFib(lambda x: x % 2 == 0)
        >>> [next(evens) for _ in range(15)]
        [0, 2, 8, 34, 144, 610, 2584, 10946, 46368, 196418, 832040, 3524578, 14930352, 63245986, 267914296]
        >>> seq = genFib(lambda x: x > 20 and x % 2)
        >>> next(seq)
        21
        >>> next(seq)
        55
        >>> next(seq)
        89
        >>> next(seq)
        233
        >>> next(seq)
        377
        >>> next(seq)
        987
        >>> next(seq)
        1597
        >>> next(seq)
        4181
        >>> evens = genFib(lambda x: x % 2 == 0)
        >>> sum([next(evens) for _ in range(50)])
        3080657373857639014791750813074
        >>> odds = genFib(lambda x: x % 2 == 1)
        >>> [next(odds) for i in range(25)]
        [1, 1, 3, 5, 13, 21, 55, 89, 233, 377, 987, 1597, 4181, 6765, 17711, 28657, 75025, 121393, 317811, 514229, 1346269, 2178309, 5702887, 9227465, 24157817]
        >>> ends_with_5 = genFib(lambda x: x % 10 == 5)
        >>> [next(ends_with_5) for i in range(10)]
        [5, 55, 6765, 75025, 9227465, 102334155, 12586269025, 139583862445, 17167680177565, 190392490709135]

    '''
    # YOUR CODE STARTS HERE
    pass


if __name__=='__main__':
    import doctest
    doctest.run_docstring_examples(matrixCalculator, globals(), name='HW3',verbose=True)