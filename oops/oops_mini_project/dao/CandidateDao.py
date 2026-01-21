class CandidateDao:
    def create_candidate(self, candidate):
        print("candidate created at dao")
        candidate.print_candidate_info()
