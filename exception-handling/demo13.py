try:
    print("try")
except ZeroDivisionError:
    print("except")
else:
    print("else")
finally:
    print("finally")
print("rest of the code")

# output
# try
# else
# finally
# rest of the code
