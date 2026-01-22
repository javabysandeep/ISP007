import os

try:
    print("try")
    print(10 / 0)
except ZeroDivisionError:
    print("division by zero")
    os._exit(0) # stops the program
finally:
    print("finally")
print("rest of the code")

#output
# try
# division by zero