try:
    print(10 / 0)
    print("rest of the try")
    print("rest of the try")
    print("rest of the try")
    print("rest of the try")
except ZeroDivisionError:
    print("division by zero")
finally:
    print("finally statement")

print("rest of the code in file")
