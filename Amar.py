import random

small_alphabets = ['a', 'b', 'c', 'd', 'e', 'f']
capital_alphabets = ['A', 'B', 'C', 'D', 'E', 'F']
digits = [0,1,2,3,4,5,6,7,8,9]
password_length=10
choices=[small_alphabets, capital_alphabets, digits]
password = []
for i in range(password_length):
        choice = random.choice(choices)
        password.append(random.choice(choice))

print(password)
