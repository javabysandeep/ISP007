# create folders
import os

path = 'C:\\Work\\file-handling-temp\\'
for i in range(10):
    os.mkdir(path + str(i))

print('new folder or directory created')
