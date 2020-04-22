import timeit
#print(timeit.timeit('1+3', number=5000000))

input_list = range(100)

def div_by_five(num):
    if num % 5 ==0:
        return True
    else:
        return False

xyz = list(i for i in input_list if div_by_five(i))

#xyz = [i for i in input_list if div_by_five(i)]

print(timeit.timeit('''input_list = range(100)

def div_by_five(num):
    if num % 5 ==0:
        return True
    else:
        return False

xyz = list(i for i in input_list if div_by_five(i))''', number= 5000))