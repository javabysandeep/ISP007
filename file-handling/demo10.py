with open("C:\\Work\\ISP007\\file-handling-temp\\shubham11.py", "r") as file:
    content = file.read()
    print(content)
    print(file.tell())
    file.seek(0)
    print(file.tell())
    print(file.read(10))

#FileNotFoundError --> trying to read the file which is not present