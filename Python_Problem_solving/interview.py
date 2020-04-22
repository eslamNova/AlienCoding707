# numbers = [45, 22, 14, 65, 97, 72]
# for i,num in enumerate(numbers, start=52):
#     print(i, num)

numbers = [4, 2, 1, 6, 9, 7]
def square(x):
    return x*x

print(list(map(square, numbers)))

print([square(x) for x in numbers])