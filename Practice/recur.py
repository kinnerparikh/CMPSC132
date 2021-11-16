def ps(brackets, dots):
    if (brackets != 0):
        return "[" + ps(brackets - 1, dots) + "]"
    elif (dots == 1):
        return '.'
    return '.' + ps(brackets, dots - 1)

#print(ps(4, 4))
def _hash(key):
    return ord(key[ 0 ]) + ord(key[ 1 ])


key = 'Ca'
print(_hash(key) % 101)

#63, 64, 65, 66, 67, 68, 100