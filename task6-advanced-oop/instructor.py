from person import Person
class Instructor(Person):
    def __init__(self,instructors=None,students=None,course=None,enrolled=None):
        if instructors is None:
          instructors = []
        super().__init__(instructors,students,course,enrolled)
        self.instructor = instructors

    def inst(self):
        print(self.instructor)
        Instruct_name=str(input("Enter Name of instructor:"))
        if isinstance(self.instructor, list):
            self.instructor.append(Instruct_name)
            for x in self.instructor:
                if Instruct_name == x:
                    return f"Welcome Instructor:{Instruct_name}"
                else:
                    return "Instructor Not found"
        else:
            print("Not list")
        
    def instructor_role(self):
        ASS_NAME=str(input("Enter name of Assitant lecture :"))
        for x in self.assist_teacher.keys():
            if ASS_NAME == x:
                mark_teacher=str(input("Enter marks of {ASS_NAME} :"))
                self.assist_teacher[ASS_NAME]=mark_teacher
            else:
                print("This assistant lecture not found")