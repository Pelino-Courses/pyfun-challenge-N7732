class Person:
    def __init__(self,instructors: list = None ,students:dict = None, course: list = None, enrolled: dict = None):
        if instructors is None:
            instructors=[]
        elif students is None:
            students={}
        elif course is None:
            course=[]
        elif enrolled is None:
            enrolled={}
            
        self.instructors=[]
        self.students={}#store student name as key and thier marks list
        self.course=["Python","Web design","IS&T","Mathematics","Drawing","English"] #course marks
        self.assist_teacher={}#store teacher names and marks(self.teacher_marks)
        self.enrolled={}#course name and self.student
        self.teacher_marks=[]#store teacher marks
    def people(self):
         print("==Welcome in Administratiion==\n\n")
         instructor_reg=str(input("Enter Instructor name:"))
         self.instructors.append(instructor_reg)
         assistant_reg=str(input("Enter name of assistant lecture:"))
         self.assist_teacher[assistant_reg]=0
         return f"{self.instructors} and {self.assist_teacher}"

         
         