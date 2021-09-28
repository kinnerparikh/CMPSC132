def get_lines(n):
    if n <= 1:
        return '*'
    else:
        return get_lines(n - 1) + '\n' + '*'*n

print(get_lines(5))