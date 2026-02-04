# read data from csv file
import os.path
import csv

if os.path.isfile('C:\\Users\\sande\\Downloads\\customers-100.csv'):
    with open('C:\\Users\\sande\\Downloads\\customers-100.csv') as f:
        content = csv.reader(f)
        for line in content:
            for word in line:
                print(word,"\t\t",end='')
            print()
else:
    print('file not exist')
