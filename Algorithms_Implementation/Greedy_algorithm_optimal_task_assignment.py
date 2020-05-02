# Greedy approach
# 1- Sort
# pick longest + shortest

# O(n log n)

A = [6,3,2,7,5,5]

A = sorted(A)

for i in range(len(A)//2):
    print(A[i], A[~i]) #not i == ~0 -> -1
