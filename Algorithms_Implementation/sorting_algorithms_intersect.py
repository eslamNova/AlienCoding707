A = [2,3,3,5,7,11]
B = [3,3,7,15,31]

# general solution

# print(set(A).intersection(B))


# O(n + m)
def intersect_sorted_array(A, B):
    S = []
    i = 0
    j = 0
    while i < len(A) and j < len(B):
        if A[i] == B[j]:
            if i == 0 or A[i] != A[i-1]:
                S.append(A[i])
            j += 1
            i += 1
        elif A[i] < B[j]:
            i += 1
        else:
            j += 1
    # for i in A:
    #     for j in B:
    #         if i == j:
    #             S.append(i)
    return S


print(intersect_sorted_array(A, B))