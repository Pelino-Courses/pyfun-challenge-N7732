from person import Person
class Course(Person):
    def __init__(self,instructors=[],students={},course=[],enrolled={}):
        super().__init__(instructors,students,course,enrolled)
    def course_details(self):
        choice=int(input("School:\n1.School of ICT\n2.School of Engineerig"))
        if choice==1:
            print("Course:\n1.Python\n2.Web design\n3.IS&T")
        elif choice==2:
            print("Course:\n1.Mathematis\n2.Drawing\n3.English")
        else:
            return f"Invalid"
    def add_course(self):
        subject=str(input("Ënter new course :"))
        self.course.append(subject)