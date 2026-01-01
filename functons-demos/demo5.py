# write function to add two numbers and return the addition

# function definition
def calculate(number1, number2):
    return (number1 + number2,
            number1 - number2,
            number1 * number2,
            number1 / number2,
            number1 // number2)

# function call
print(calculate(10, 20))