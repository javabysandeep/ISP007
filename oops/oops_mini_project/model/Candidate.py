class Candidate:
    def __init__(self, candidate_id, name, skills, experience, expected_salary, status, applied_jobs):
        self.__candidate_id = candidate_id
        self.__name = name
        self.__skills = skills
        self.__experience = experience
        self.__expected_salary = expected_salary
        self.__status = status
        self.__applied_jobs = applied_jobs

    def print_candidate_info(self):
        print("candidate id: " + str(self.__candidate_id))
        print("name: " + self.__name)
        print("skills: " + str(self.__skills))
        print("experience: " + str(self.__experience))
        print("expected_salary: " + str(self.__expected_salary))
        print("status: " + self.__status)
        print("applied_jobs: " + str(self.__applied_jobs))

    def get_candidate_id(self):
        return self.__candidate_id

    def get_name(self):
        return self.__name

    def get_skills(self):
        return self.__skills

    def get_experience(self):
        return self.__experience

    def get_expected_salary(self):
        return self.__expected_salary

    def get_status(self):
        return self.__status

    def get_applied_jobs(self):
        return self.__applied_jobs

    def set_candidate_id(self, candidate_id):
        self.__candidate_id = candidate_id

    def set_name(self, name):
        self.__name = name

    def set_skills(self, skills):
        self.__skills = skills

    def set_experience(self, experience):
        self.__experience = experience

    def set_expected_salary(self, expected_salary):
        self.__expected_salary = expected_salary

    def set_status(self, status):
        self.__status = status

    def set_applied_jobs(self, applied_jobs):
        self.__applied_jobs = applied_jobs
