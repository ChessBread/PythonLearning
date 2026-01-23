# class variable = shared amoung all instances of a class
#                   Defined outside the constructor
#                   Allow you to share data amoung all objects crated form a class




class Student:

    class_year = 2025
    num_students = 0


    def __init__(self, name , age):
        self.name = name
        self.age = age
        Student.num_students += 1

student1 = Student("James", 30)

student2 = Student("Patrick" , 35)



print(f"My gratuating year was {Student.class_year} and we were {Student.num_students} students in the class")
print(Student.name)
print