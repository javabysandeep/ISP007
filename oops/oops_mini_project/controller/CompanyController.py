from oops.oops_mini_project.model.Company import Company
from oops.oops_mini_project.service.CompanyService import CompanyService
from oops.oops_mini_project.dao.CompanyDao import CompanyDao


class CompanyController:
    def __init__(self, company_service):
        self.company_service = company_service

    def create_company(self, company):
        self.company_service.create_company(company)

dao=CompanyDao()
service = CompanyService(dao)
controller = CompanyController(service)
modelCompany = Company(101, "IT Shaala", "itshaala.com", "Pune")
controller.create_company(modelCompany)
