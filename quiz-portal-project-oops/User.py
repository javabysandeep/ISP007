class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

    def login(self):
        print(f"{self.user_id} logged in")


class Student(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self.score = 0

    def attempt_quiz(self):
        print(f"{self.user_id} is attempting a quiz")


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        print('Admin is creating a quiz')


class Question:
    def __init__(self, question_text, options, correct_option):
        self.question_text = question_text
        self.options = options
        self.correct_option = correct_option

    def display_question(self):
        print(f"{self.question_text}")
        for i, opt in enumerate(self.options, 1):
            print(f"{i}.{opt}")

    def is_correct(self, user_choice):
        return self.correct_option == self.options[user_choice - 1]


class Quiz:
    def __init__(self, title):
        self.title = title
        self.questions = []

    def add_question(self, question):
        self.questions.append(question)

    def start(self, student):
        print(f"{student.user_id} is starting to quiz")
        calculate_score = 0

        for question in self.questions:
            question.display_question()
            choice = int(input("Enter your choice: "))
            if question.is_correct(choice):
                calculate_score += choice

        student.score = calculate_score
        return calculate_score


class Result:
    def __init__(self, student, quiz, student_score):
        self.student = student
        self.quiz = quiz
        self.score = student_score

    def display_result(self):
        print(f"Student: {self.student.name}")
        print(f"Quiz: {self.quiz.title}")
        print(f"Score: {self.score}")


class Controller:
    def __init__(self):
        self.users = []
        self.quizzes = []

    def add_user(self, user):
        self.users.append(user)

    def add_quiz(self, quiz):
        self.quizzes.append(quiz)


# create student
s1 = Student(1, 'Sahil')

# create quiz
quiz1 = Quiz('Python Basics')

# create questions
question1 = Question("what is python?", ["Snake", "def", "Game", "Car", "programming language"], 'programming language')
question2 = Question("which keyword is used to create function?", ["fun", "method", "def", "method"], 'def')

# add questions to quiz
quiz1.add_question(question1)
quiz1.add_question(question1)
quiz1.add_question(question1)
quiz1.add_question(question1)
quiz1.add_question(question1)
quiz1.add_question(question2)
quiz1.add_question(question2)
quiz1.add_question(question2)
quiz1.add_question(question2)
quiz1.add_question(question2)

# start the quiz
score = quiz1.start(s1)

# show result
result = Result(s1, quiz1, score)
result.display_result()
