def is_positive_integer(string):
    if string.isdigit():
        return True
    return False

print(is_positive_integer("123"))
print(is_positive_integer("-456"))
print(is_positive_integer("12.3"))
print(is_positive_integer("abc"))
