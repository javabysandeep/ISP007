class User:
    def __init__(self, id, email, phone, username, password):
        self.id = id
        self.email = email
        self.phone = phone
        self.username = username
        self.password = password

    def login(self):
        print("login user")

    def logout(self):
        print("logout user")


class Admin(User):
    pass


class Candidate(User):
    def __init__(self, candidate_id, name, skills, experience, expected_salary, status, applied_jobs):
        self.candidate_id = candidate_id
        self.name = name
        self.skills = skills
        self.experience = experience
        self.expected_salary = expected_salary
        self.status = status
        self.applied_jobs = applied_jobs


class Recruiter(User):
    pass
