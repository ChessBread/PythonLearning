# nested class = a class defined inside another class
#          Class outer:
#              Class inner:

# benefits = allows you to logically group classes that are closely related
#           encapsulates private details that aren't relevant outside of the outer class
#           keeps the namespace clean; reduces the possibility of naming conflicts


class Company:
    class Employee:
        def __init__(self, name, position):
            self.name = name
            self.position = position
        
        def get_details(self):
            return f"{self.name}, {self.position}"


    def __init__(self, company_name):
        self.company_name = company_name
        self.employees = []
    
    def add_employee(self, name, position):
        new_employee = self.Employee(name, position)
        self.employees.append(new_employee)


    def list_employees(self):
        return [employee.get_details() for employee in self.employees]



company1= Company("TechCorp")
company2 = Company("DesignInc")

company2.add_employee("Diana", "Artist")
company2.add_employee("Ethan", "Engineer")
company2.add_employee("Sheldon", "Scientist")

company1.add_employee("Alice", "Developer")
company1.add_employee("Bob", "Designer")
company1.add_employee("Charlie", "Manager")

for employee in company2.list_employees():
    print(employee)

