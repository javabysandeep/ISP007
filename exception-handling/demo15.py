try:
    print("try")
    raise ZeroDivisionError() # similar to 10/0
except ZeroDivisionError:
    print("except")
else:
    print("else")
finally:
    print("finally")
print("rest of the code")

# output
# try
# except
# finally
# rest of the code
