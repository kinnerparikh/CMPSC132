from typing import List, final


def finalQuizScore(h,l,r,q,n,p):
 a=round(900-h*3-l*2-r*1.5-q-n-p/2)
 r='Sorry, y'if a>100 else'Y'
 return(r+f'ou would need a {a}% on the final quiz to get an A-.')

def getEvenCount(num):
    if num < 0:
        num = num * (-1)
    counter = 0
    while num > 0:
        if num % 2 == 0:
            counter += 1
        num = num // 10
    
    return counter


def product(nums):
    leftProd = list()
    leftProd.append(1)

    for i in range(1, len(nums)):
        leftProd.append(leftProd[i - 1] * nums[i - 1])
    
    rightSide = 1
    for i in range(len(nums) - 1, -1, -1):
        leftProd[i] *= rightSide
        rightSide *= nums[i]
    
    return leftProd

arr = [1, 2, 3, 4]


def prod(nums):
    rightArr = [1]
    leftArr = [1]

    for i in range(1, len(nums)):
        leftArr.append(leftArr[i - 1] * nums[i - 1])
    
    for i in range(1, len(nums)):
        rightArr.append(rightArr[i - 1] * nums[len(nums) - i])

    finalArr = list()
    for i in range(0, len(nums)):
        finalArr.append(leftArr[i] * rightArr[len(nums) - 1 - i])
    
    return finalArr

# [1, 2, 3, 4]
# left = [1, 1, 2, 6]
# right = [1, 4, 12, 24]
prod(arr)
