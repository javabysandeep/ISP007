# read data from csv file
import os.path
import csv


class Customer:
    def __init__(self, index, customer_id, first_name, last_name, company,
                 city, country, phone1, phone2, email, subscription_date, website):
        self.index = index
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.company = company
        self.city = city
        self.country = country
        self.phone1 = phone1
        self.phone2 = phone2
        self.email = email
        self.subscription_date = subscription_date
        self.website = website


customer_list = []
if os.path.isfile('C:\\Users\\sande\\Downloads\\customers-100.csv'):
    with open('C:\\Users\\sande\\Downloads\\customers-100.csv') as f:
        content = csv.reader(f)
        for line in content:
            obj =Customer()
            for word in line:

        customer_list.append(obj)

else:
    print('file not exist')
