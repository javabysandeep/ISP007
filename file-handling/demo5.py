file = open("C:\\Work\\ISP007\\file-handling-temp\\shubham.py", "r")
lines = file.readlines()

for line in lines:
    print(line)

file.close()
