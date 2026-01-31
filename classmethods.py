# allows operatuions related to the class itself rather than to instances of the class
# take (self) as the first parameter, which represents the class itself


class student:


    count = 0
    total_gpa = 0.0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        student.count += 1
        student.total_gpa += gpa

    # instance method
    def get_info(self):
        return f"{self.name} has a GPA of {self.gpa}"
    


    @classmethod
    def get_count(cls):
        return f"Total number of students: {cls.count}"
    

    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0.0
        else:
            return f"{cls.total_gpa / cls.count:.2f}"
    


student1 = student("John", 3.5)
student2 = student("Jane", 3.8)


print(student.get_count())  # Total number of students: 2
print(student.get_average_gpa())  # Average GPA: 3.65