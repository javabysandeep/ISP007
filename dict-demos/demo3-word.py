#Q1. find the occurrence of each word
given_string = 'hello good morning hello good'
words=given_string.split(" ")

dict_word_count={}
for word in words:
    if word in dict_word_count:
        dict_word_count[word] += 1
    else:
        dict_word_count[word] = 1

print(dict_word_count)
print("printing dictionary")
for entry in dict_word_count:
    print(entry, dict_word_count[entry])






















#Q4. find the second non repeat character