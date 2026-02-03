with open("C:\\Work\\ISP007\\file-handling-temp\\shubham.py", "r") as file:
    print(file.tell()) #cursor=0
    print(file.read(2))# it will read first 2 characters
    print(file.tell()) #cursor=2
    print(file.read(5)) # it will read next 5 characters
    print(file.tell()) #cursor = 7

