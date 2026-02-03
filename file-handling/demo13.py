# Find the number of lines, words and characters present in the file?
import os


if os.path.isfile("C:\\Users\\sande\\Downloads\\customers-100.csv"):
    with open('C:\\Users\\sande\\Downloads\\customers-100.csv') as f:
        for line in f:
            print(line)
