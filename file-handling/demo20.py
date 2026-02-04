# create folders - C:\Work\file-handling-temp
import os

with open('student-details.txt', 'rb') as f:
    current_working_directory = os.path.abspath('student-details.txt')
    cwd = os.getcwd()
    print(cwd)
    print(current_working_directory)
