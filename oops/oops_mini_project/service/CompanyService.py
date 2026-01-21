class CompanyService:
    def __init__(self, company_dao):
        self.company_dao = company_dao

    def create_company(self, company):
        self.company_dao.create_company(company)

