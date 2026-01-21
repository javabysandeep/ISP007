class CandidateService:
    def __init__(self, candidate_dao):
        self.candidate_dao = candidate_dao

    def create_candidate(self, candidate):
        self.candidate_dao.create_candidate(candidate)
