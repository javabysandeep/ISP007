from oops.oops_mini_project.dao.CandidateDao import CandidateDao
from oops.oops_mini_project.model.Candidate import Candidate
from oops.oops_mini_project.service.CandidateService import CandidateService


class CandidateController:
    def __init__(self, candidate_service):
        self.candidate_service = candidate_service

    def create_candidate(self, candidate):
        self.candidate_service.create_candidate(candidate)


dao = CandidateDao()
service = CandidateService(dao)
controller = CandidateController(service)
modelCandidate = Candidate(101, "Ali", "React", "1 year", "10k", "New", "0")
controller.create_candidate(modelCandidate)
