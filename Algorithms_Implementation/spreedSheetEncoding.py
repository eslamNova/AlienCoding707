def spreedSheet_encode_column(str_col):
    num = 0 
    count = len(str_col) - 1 
    for char in str_col:
        num += 26**count * (ord(char)-64)
        count -=1
    return num


# Encoding Test
print(spreedSheet_encode_column("A"))
print(spreedSheet_encode_column("AA"))
print(spreedSheet_encode_column("ZZ"))