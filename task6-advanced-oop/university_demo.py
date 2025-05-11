from person import Person
from student import Student
from enrollment import enroll
from teaching_assistant import Ass_teacher
#from teaching_assistant import teaching_assistant
from instructor import Instructor
from course import Course
shared_instructors = []
shared_students = {}
shared_courses = ["Python", "Web design", "IS&T", "Mathematics", "Drawing", "English"]
shared_enrolled = {}
counter = 0
while(True):
    def main():
        print("==University of Rwanda==\n")
        choice=int(input("Enter you\n1.Admin\n2.Student\n3.course\n4.Instuctor\n5.Assitant\n6.enrollementUniversity information\nEnter choice:"))
        if choice==1:
            Obje=Person(shared_instructors,shared_students,shared_courses,shared_enrolled)
            print(Obje.people())
        elif choice==2:
            obje1=Student(shared_instructors,shared_students,shared_courses,shared_enrolled)
            print(obje1.student_details(),obje1.sum_grade())
        elif choice==3:
            obje2=Course(shared_instructors,shared_students,shared_courses,shared_enrolled)
            print(obje2.course_details(),obje2.add_course())
        elif choice==6:
            obje3=enroll(shared_instructors,shared_students,shared_courses,shared_enrolled)
            print(obje3.enrollement_detaild(),obje3.delete_enrollemnent())
        elif choice==4:
            obje4=Instructor(shared_instructors,shared_students,shared_courses,shared_enrolled)
            print(obje4.inst()) 
            print(obje4.instructor_role())
        elif choice==5:
            obje5=Ass_teacher(shared_instructors,shared_students,shared_courses,shared_enrolled) 
            print(obje5.teacher_role(),obje5.my_marks())
        else:
            print("Invalid choice")
    if __name__ == "__main__":
        main()
    counter +=1   