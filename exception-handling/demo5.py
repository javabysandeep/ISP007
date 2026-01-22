try:
    number1 = int(input("enter number1"))
    number2 = int(input("enter number2"))
    print(number1 / number2)

except ZeroDivisionError:
    print("division by zero")

except ValueError:
    print("invalid input")

finally:
    print("finally statement")

print("rest of the file")
