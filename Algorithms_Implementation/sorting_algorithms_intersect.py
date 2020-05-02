A = [2,3,3,5,7,11]
B = [3,3,7,15,31]

# general solution

# print(set(A).intersection(B))



def intersect_sorted_array(A, B):
    S = []
    for i in A:
        for j in B:
            if i == j:
                S.append(i)
    return set(S)


print(intersect_sorted_array(A, B))