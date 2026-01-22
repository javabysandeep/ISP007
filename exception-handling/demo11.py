try:
    print("try")
    print(10 / 0)
finally:
    print("finally")
print("rest of the code")

# output :
# try
# finally
# Traceback (most recent call last):
#   File "C:\Work\ISP007\exception-handling\demo11.py", line 3, in <module>
#     print(10 / 0)
#           ~~~^~~
# ZeroDivisionError: division by zero
