# inheritance: single level


class Person():

    def __init__(self, name):
        self.name = name

    def show_name(self):
        print(f"Name: {self.name}")


class Teacher(Person):

    def __init__(self, name, email):
        Person.__init__(self, name)
        self.email = email
        self.is_admin = True

    def check_admin_status(self):
        print(f"Can Teach: {self.is_admin}")


john = Teacher("John", "john@mail.com")
john.show_name()
john.check_admin_status()
