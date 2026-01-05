# return strings whose count of characters >5

names = ["Madhavi", "Amar", "Swagat", "Sahil", "Shubham", "Hanumant"]
print(list(filter(lambda x: len(x) > 5, names)))
