try:
    number1 = int(input("enter number1"))
    number2 = int(input("enter number2"))
    print(number1 / number2)
    result = []
    print(result.index(10))

except ZeroDivisionError:
    print("invalid input")

except:
    print("generic handler")
finally:
    print("finally statement")

print("rest of the file")
