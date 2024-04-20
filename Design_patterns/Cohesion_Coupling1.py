"""
In the below example, the Student class has low cohesion because it has multiple responsibilities: 
printing student details, checking scholarship eligibility, saving data to a database, and sending email.
These responsibilities are not closely related to the core concept of a student, violating the 
Single Responsibility Principle (SRP) of the SOLID principles.

Additionally, the Student class has high coupling because it directly interacts with external components 
like the database and email notification system. 
This tight coupling makes it harder to change or replace those external components without modifying the 
Student class, violating the Dependency Inversion Principle (DIP) of the SOLID principles.
"""

class Student:
    def __init__(self, name, age, gpa):
        self.name = name
        self.age = age
        self.gpa = gpa

    def print_student_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"GPA: {self.gpa}")

    def is_eligible_for_scholarship(self):
        return self.gpa >= 3.5

    def save_to_database(self):
        # Code to save student data to a database
        print("Student data saved to database")

    def send_email_notification(self):
        # Code to send an email notification
        print("Email notification sent")


if __name__ == "__main__":
    student = Student("Ricky", 20, 3.8)
    student.print_student_details()
    if student.is_eligible_for_scholarship():
        print("Eligible for scholarship")
        student.save_to_database()
        student.send_email_notification()


############################################################################################
from abc import ABC, abstractmethod
from typing import Any

class StudentInfo:
    """
    This class will have all the details of the student
    """
    def __init__(self, name: str, age: str, gpa: float, email: str =None):
        self.name = name
        self.age = age
        self.gpa = gpa
        self.email = email

    def print_student_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"GPA: {self.gpa}")
        print(f"Email: {self.email}")


class Repo(ABC):
    """
    This class will have all the methods related to the database for student repo
    """
    @abstractmethod
    def get_details(self, id: Any):
        pass

    @abstractmethod
    def get_all_details(self, limit: int , offset: int):
        pass

    @abstractmethod
    def save_to_database(self, stu_details):
        pass

    @abstractmethod
    def delete_from_database(self, id: Any):
        pass


class StudentRepo(Repo):
    """
    This class will have all the methods related to the database for student repo
    """
    def get_details(self, id: int):
        # code to get a particular student detail from db based on id
        print("Student data fetched from database")

    def get_all_details(self, limit: int, offset: int):
        # code to get all the student details from db
        print("All Student data fetched from database")

    def save_to_database(self, stu_details: StudentInfo):
        # code to save student details to db
        print("Student data saved to database")

    def delete_from_database(self, id: int):
        # code to delete student details from db based on id
        print("Student data with id:", id, "deleted from database")


class NotificationService:
    """
    This class will have all the methods related to the notification system
    """
    
    @abstractmethod
    def send_email_notification(self, from_email, to_email, subject, body):
        # Code to send an email notification
        print("Email notification sent")
        return True

    # we can send other notifications in future (sms, gmail, twitter, etc)

class EligibilityChecker:
    """
    This class will have all the methods related to the eligibility checker
    """
    MIN_GPA_FOR_SCHOLARSHIP = 3.5

    @staticmethod
    def is_eligible_for_scholarship(student: StudentInfo) -> bool:
        return student.gpa >= EligibilityChecker.MIN_GPA_FOR_SCHOLARSHIP
    
    # we can check other criteria here


if __name__ == '__main__':
    student = StudentInfo("Ricky", 20, 3.8, "studen1t@email.com")
    student.print_student_details()

    repo = StudentRepo()
    repo.save_to_database(student)

    if EligibilityChecker.is_eligible_for_scholarship(student):
        print("Eligible for scholarship")
    else:
        print("Not eligible for scholarship")

    if student.email:
        NotificationService().send_email_notification(
            from_email="fromemail@example.com", 
            to_email=student.email,
            subject="subject", 
            body="body"
        )
    else:
        print("Email not found")