class Student:
    def __init__(self, name, student_id, courses):
        self.name = name
        self.student_id = student_id
        self.courses = courses

    def show_info(self):
        print(f"Name: {self.name} \nStudent ID: {self.student_id} \nCourses:")
        for course in self.courses:
            print("     -" + course)
        print()

    def add_course(self, course):
        if course not in self.courses:
            self.courses.append(course)
            print(f"{self.name}'s courses:")
            for course in self.courses:
                print("     -" + course)
            print()
        else:
            print(f"{self.name} is already registered for {course} course\n")


student1 = Student("Nika", "001", ["Math", "Biology", "Literature"])
student1.show_info()
student1.add_course("Art")

student2 = Student("Tako", "002", ["Chemistry", "Physics", "Art"])
student2.show_info()
student2.add_course("Art")
student2.add_course("English")
