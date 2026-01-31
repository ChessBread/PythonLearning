# a method that belonghs to a class rather than any object from that class (instance_method)
# static method does not take self or cls as the first parameter
# static methods are used to group functions which have some logical connection with a class to the class



from logging import info


class Employee:

    def __init__(self, name, position):
        self.name = name
        self.position = position


    def get_info(self):
        return f"{self.name} = {self.position}"
    


    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager", "Developer", "Designer", "Intern"]
        return position in valid_positions
    

emp1 = Employee("Alice", "Developer")
emp2 = Employee("Bob", "Chef")
emp3 = Employee("Charlie", "Manager")
emp4 = Employee("Diana", "Artist")

print(Employee.is_valid_position(emp1.position))  # True
print(emp2.get_info())
print(Employee.is_valid_position(emp2.position))  # False
print(emp3.get_info())