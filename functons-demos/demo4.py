import random

def generate_otp():
    return random.randint(100000, 999999)

def find_lucky(values):
    return random.choice(values)



print("otp is ", generate_otp())
print("lucky one is ",find_lucky(['Hanumanut', 'Shubham','Amar','Sahil','Swagat','Sandeep']))

