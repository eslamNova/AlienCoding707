x = 70
y = 50000


def recursive_multiply(x, y):
    # to handle recursion threshold
    if x < y:
        return recursive_multiply(y, x)
    if y == 0:
        return 0
    return x + recursive_multiply(x, y-1)


print(x*y)
print(recursive_multiply(x, y))
