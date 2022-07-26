# display employee data using classes and object
class Employee:

    def __init__(self, name, company, id, salary):
        self.name = name
        self.company = company
        self.id = id
        self.salary = salary

    def get_data(self):
        print(f"Name: {self.name}")
        print(f"Company: {self.company}")
        print(f"Id: {self.id}")
        print(f"Salary: ${self.salary}")


john = Employee("John", "Microsoft", "001", 2000.0)
john.get_data()