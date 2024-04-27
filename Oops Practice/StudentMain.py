from Student import *

if __name__ == '__main__':
    # CREATING OBJECTS MANUALLY
    '''
    stu1 = Student('sabari', 'CS', 3)
    stu2 = Student('arasu', 'Tamil', 3)
    stu3 = Student('saran', 'EnglisH', 3)
    
    students = [stu1, stu2, stu3]
    for stu in students:
        print(stu.name)
    '''
    # CREATE OBJECT DYNAMICALLY
    size = int(input("How many students ?"))
    # DEFINING EMPTY LIST AND DICTIONARY
    students = list()

    for i in range(size):
        name = input("Enter name:")
        dpt = input('Enter dpt:')
        year = int(input('Enter year:'))
        # ADDING STUDENT DETAILS TO LIST
        students.append(Student(name, dpt, year))

        if i < size - 1:
            print("next student--->")

    Student.student_details()
