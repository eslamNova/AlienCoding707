in_str = "AlienOwlLove"

print(len(in_str))


def iterative_str_len(in_str):
    count = 0
    for _ in range(len(in_str)):
        count += 1
    return count


def recursive_str_len(in_str):
    if in_str == '':
        return 0
    return 1 + recursive_str_len(in_str[1:])


print(iterative_str_len(in_str))
print(recursive_str_len(in_str))
