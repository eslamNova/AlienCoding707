a = 5
b = 6
c = 10
n = 5
for i in range(n):
    for j in range(n):
        x = i * i
        y = j * j
        z = i * j
for k in range(n):
    w = a*k + 45
    v = b*b
d = 33


# The number of assignment operations is the sum of four terms. The first term is the constant 3, representing the three assignment statements at the start of the fragment. The second term is 3n2, since there are three statements that are performed n2 times due to the nested iteration. The third term is 2n, two statements iterated n times. Finally, the fourth term is the constant 1, representing the final assignment statement. This gives us T(n)=3+3n2+2n+1=3n2+2n+4. By looking at the exponents, we can easily see that the n2 term will be dominant and therefore this fragment of code is O(n2)
