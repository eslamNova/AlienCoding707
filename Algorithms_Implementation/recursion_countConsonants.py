in_1 = "alien m"
in_2 = "AlienOwlLoveU"

vowels = "aeiou"
vowel = ['a', 'e', 'i', 'o', 'u']


def iterative_count_consonants(in_str):
    count = 0
    for i in range(len(in_str)):
        if in_str[i].lower() not in vowels and in_str[i].isalpha():
            count += 1
    return count


def recursive_count_consonants(in_str):
    if in_str == '':
        return 0
    if in_str[0].lower() not in vowels and in_str[0].isalpha():
        return 1 + recursive_count_consonants(in_str[1:])
    else:
        return recursive_count_consonants(in_str[1:])


print(iterative_count_consonants(in_1))
print(iterative_count_consonants(in_2))

print(recursive_count_consonants(in_1))
print(recursive_count_consonants(in_2))
