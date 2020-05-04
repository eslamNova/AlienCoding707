is_per_1 = "isa"
is_per_2 = "asi"

not_per_1 = "Not"
not_per_2 = "top"

# time >> O(n log n)
# space >> O(1)
def is_perm_1(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()

    if len(str1) != len(str2):
        return False
    str1 = ''.join(sorted(str1))
    str2 = ''.join(sorted(str2))

    n = len(str1)

    for i in range(n):
        if str1[i] != str2[i]:
            return False
    return True

print(is_perm_1(is_per_1, is_per_2))
print(is_perm_1(not_per_1, not_per_2))


def is_perm_2(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()

    if len(str1) != len(str2):
        return False
    
    d = dict()

    for i in str1:
        if i in d:
            d[i] -= 1
        else:
            d[i] = 1
    for i in str2:
        if i in d:
            d[i] -= 1
        else:
            d[i] = 1
    return all(value == 0 for value in d.values())

print(is_perm_2(is_per_1, is_per_2))
print(is_perm_2(not_per_1, not_per_2))