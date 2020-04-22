input_list = [5,7,2,67,20,1,4,3]

def div_by_five(num):
    if num % 5 ==0:
        return True
    else:
        return False

xyz = (i for i in input_list if div_by_five(i))

# xyz = []
# for i in input_list:
#     if div_by_five(i):
#         xyz.append(i)

# for i in xyz:
#     print(i)
#[print(i) for i in xyz]
# print(xyz)
xyz = [i for i in input_list if div_by_five(i)]
# print(xyz)
# [print(i) for i in xyz]


# for i in range(5):
#     for ii in range(5):
#         print(i, ii)

# xyz = ([[i,ii] for ii in range(5)] for i in range(5))
# print(xyz)
# for i in xyz:
#     print(i)


