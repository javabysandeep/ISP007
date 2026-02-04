# write data to a csv file
import os.path
import csv

if os.path.isfile('C:\\Users\\sande\\Downloads\\customers-100.csv'):
    with open('C:\\Users\\sande\\Downloads\\customers-100.csv', 'a+', newline='') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(
            ['101', '2354a0E336A91A12', 'Amar', 'Bodhale', 'IT Shaala', 'Pune', 'India', '123', '', 'amar@gmail.com',
             '19-08-2020', 'itshaala.com'])
        print('row added successfully')

else:
    print('file not exist')
