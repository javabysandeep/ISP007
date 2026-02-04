# read data from csv file
import os.path

if os.path.isfile('C:\\Users\\sande\\Downloads\\customers-100.csv'):
    with open('C:\\Users\\sande\\Downloads\\customers-100.csv') as f:
        content = f.readlines()
        for line in content:
            print(line)
else:
    print('file not exist')
