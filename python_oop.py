class Student:
    def __init__(self, name, age, grade_level):
        self.name = name
        self.age = age
        self.grade_level = grade_level
        
    def print_info(self):
        print(f"Student: {self.name}, Age: {self.age}, Grade Level: {self.grade_level}")

class Teacher:
    def __init__(self, name, age, subject):
        self.name = name
        self.age = age
        self.subject = subject
        
    def print_info(self):
        print(f"Teacher: {self.name}, Age: {self.age}, Subject: {self.subject}")

class School:
    def __init__(self):
        self.student = Student("John", 15, "10th")
        self.teacher = Teacher("Ms. Smith", 35, "Math")
        
    def print_info(self):
        self.student.print_info()
        self.teacher.print_info()

# Create a School object and print student and teacher information
school = School()
school.print_info()
