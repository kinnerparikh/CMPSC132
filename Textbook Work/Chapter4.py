import sys

#4.9
'''
Write a short recursive Python function that finds the minimum
and maximum values in a sequence without using any loops
'''
def minMax(aList, min = sys.maxsize, max = -sys.maxsize):
    if len(aList) == 0:
        return min, max
    elif aList[0] > min and aList[0] < max:
        return minMax(aList[1:], aList[0], aList[0])
    elif aList[0] < min:
        return minMax(aList[1:], aList[0], max)
    return minMax(aList[1:], min, aList[0])


print(minMax([1, 4, 8, 1, -1, -6, 344, 999, -9999]))