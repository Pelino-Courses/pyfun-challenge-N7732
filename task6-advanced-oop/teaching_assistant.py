from student import Student
from person import Person
class Ass_teacher(Student):
    def __init__(self,instructor=[],students={},course=[],enrolled={}):
        super().__init__(instructor,students,course,enrolled)
        self.assist_teacher={}
        self.grades={}
    def teacher_role(self):
        print("++ASSITANT POTAL++\n\n")
        ass_name=str(input("Enter your assistant name:"))
        for x in self.assist_teacher.keys():
            if ass_name in x:
                print(x)
                print("Welcome Assister:{ass_name}\n\n")
                enroll=str(input("Enter Name of student goes to be enrolled:"))
                enroll_subject=str(input("Enter Subject goes to be enrolled in :"))
                if enroll_subject in self.course:
                    self.enrolled[enroll_subject]=self.students           
                    if enroll in self.students:
                        mark_student=int(input("Enter marks:"))
                        self.grade.append(mark_student)
                        return f"Welcome to Our module to This {enroll_subject} module"
                    else:
                        return f"This student not found in univesity\n"   
                else:
                    f"Not found\n"
            else:
                return f"Go to Create course!\n"
        
    def my_marks(self):
        return f"My ,marks : {self.assist_teacher}"                                                                 