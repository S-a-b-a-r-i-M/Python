class Student:
    # class_var
    student_id = 0
    students_list = dict()

    def __init__(self, name, dpt, year):
        Student.student_id += 1
        self.id = Student.student_id
        self.name = name
        self.dpt = dpt
        self.year = year
        Student.students_list[self.id] = self

    @classmethod
    def student_details(cls):
        print('------------ STUDENT DETAILS ---------------')
        for stu in Student.students_list.values():
            print(stu)

    def student_by_id(self, id):
        print("Student details for id :", id)

    def delete_student_by_id(self):
        print("Student details for id :", id)

    def __str__(self):
        return "ID : {}  NAME : {}  DEPT : {}   YEAR : {}".format(self.id, self.name, self.dpt, self.year)
