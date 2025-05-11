from person import Person
class Student(Person):
    def __init__(self,instructor=[],students={},course=[],enrolled={}):
        super().__init__(instructor,students,course,enrolled)
        self.grade=[]
    def student_details(self):
        name=str(input("Student Registration:"))   
        self.students[name]=self.grade
    def sum_grade(self):
        w=sum(self.grade)
        return f"My Grade{w}"