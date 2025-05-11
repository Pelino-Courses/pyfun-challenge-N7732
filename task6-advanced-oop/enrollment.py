from person import Person
class enroll(Person):
    def __init__(self,instructors=[],students={},course=[],enrolled={}):
        super().__init__(instructors,students,course,enrolled)
        pass
    def enrollement_detaild(self):
        return self.enrolled
    def delete_enrollemnent(self):
        name=str(input("Enter student you want to remove:"))
        if name in self.students[name]:
            print(f"Are you sure you want to remove:{name}?")
            chose=str(input("Yes/No :"))
            if chose=="Yes":
                del self.students[name]
                return self.enrolled
            elif chose=="No":
                return f"Ok"