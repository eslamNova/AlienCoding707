in_1 = "alienOwllove"
in_2 = "AlienOwlLove"
in_3 = "alienowllove"


def find_uppercase_iterative(in_Str):
    for i in range(len(in_Str)):
        if in_Str[i].isupper():
            return in_Str[i]
    return "No Uppercase Found, don't be sad, take those instead: (I, S, L, A, M) :3"


def find_uppercase_recursive(in_str, idx=0):
    if in_str[idx].isupper():
        return in_str[idx]
    if idx == len(in_str) - 1:
        return "No Uppercase Found, don't be sad, take those instead: (I, S, L, A, M) :3"
    return find_uppercase_recursive(in_str, idx+1)


print(find_uppercase_iterative(in_1))
print(find_uppercase_iterative(in_2))
print(find_uppercase_iterative(in_3))

print(find_uppercase_recursive(in_1))
print(find_uppercase_recursive(in_2))
print(find_uppercase_recursive(in_3))
