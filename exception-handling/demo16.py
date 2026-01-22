# create a custom exception class
class InvalidEmailError(Exception):
    def __init__(self, value):
        self.message = value

email = input("enter your email: ")
try:
    if email.find("@") == -1:
        raise InvalidEmailError(email + " is not a valid email address")
    else:
        print(email)
except InvalidEmailError:
    print(email)
