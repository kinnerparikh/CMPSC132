def hailstone(num):
    if num == 1:
        return [1]
    elif num % 2 == 0:
        return [num] + hailstone(num//2)
    else:
        return [num] + hailstone(num*3 + 1)