def find(*strings, key):
    for string in strings:
        if string == key:
            return string
    return None


print(find("abc","abc","xyz",key="abc"))
