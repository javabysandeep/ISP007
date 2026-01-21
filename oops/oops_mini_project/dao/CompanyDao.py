class CompanyDao:
    def create_company(self, company):
        print("company created at dao")
        company.print_company_info()
