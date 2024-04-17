def is_not_blank(string):
    return bool(string and not string.isspace())


def is_blank(string):
    return not (string and string.strip())


# print(is_not_blank(""))
# print(is_not_blank(" "))
# print(is_not_blank("mike"))
# print(is_not_blank(None))

# Results
# False
# False
# True
# False


# print(is_blank(""))
# print(is_blank(" "))
# print(is_blank("mike"))
# print(is_blank(None))

# Results
# True
# True
# False
# True
