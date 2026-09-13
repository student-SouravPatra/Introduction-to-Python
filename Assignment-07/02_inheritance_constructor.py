# Assignment 7 - Program 2
# Inheritance with Constructor

class Student:
    def __init__(self, roll, name):
        self.roll = roll
        self.name = name


class UGStudent(Student):
    def __init__(self, roll, name, idp):
        super().__init__(roll, name)
        self.idp = idp

    def show(self):
        print("Roll No:", self.roll)
        print("Name:", self.name)
        print("IDP:", self.idp)


# Create UGStudent object
student = UGStudent(101, "Rahul", "IDP001")

# Display student details
student.show()
