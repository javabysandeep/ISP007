class Company:
    def __init__(self, company_id, name, website, location):
        self.__company_id = company_id
        self.__name = name
        self.__website = website
        self.__location = location

    def get_company_id(self):
        return self.__company_id

    def get_name(self):
        return self.__name

    def get_website(self):
        return self.__website

    def get_location(self):
        return self.__location

    def set_company_id(self, company_id):
        self.__company_id = company_id

    def set_name(self, name):
        self.__name = name

    def set_website(self, website):
        self.__website = website

    def set_location(self, location):
        self.__location = location

    def print_company_info(self):
        print("Company ID:", self.get_company_id())
        print("Company Name:", self.get_name())
        print("Company Website:", self.get_website())
        print("Company Location:", self.get_location())


