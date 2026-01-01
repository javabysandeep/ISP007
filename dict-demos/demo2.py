#Q1. find the occurrence of each character
s1 = 'hello good morning'
dict_char_count={}
for ch in s1:
    if ch in dict_char_count:
        dict_char_count[ch] += 1
    else:
        dict_char_count[ch] = 1

print(dict_char_count)
print("printing dictionary")
for entry in dict_char_count:
    print(entry, dict_char_count[entry])






















#Q4. find the second non repeat character