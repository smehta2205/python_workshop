class Person:
    def __init__(self, fname, lname):
        self.first_name = fname
        self.last_name = lname

    def __str__(self):
        return "Name is {} {}".format(self.first_name, self.last_name)

class Employee(Person):
    def __init__(self, fname, lname, emp_code):
        super(Employee, self).__init__(fname, lname)
        self.emp_code = emp_code

    def __str__(self):
        return super(Employee, self).__str__() + \
        " and employee code is {}".format(self.emp_code)

class Student(Person):
    def __init__(self, fname, lname, id_no):
        super(Student, self).__init__(fname, lname)
        self.id_no = id_no

    def __str__(self):
        return super(Student, self).__str__() + \
        " and id_no is {}".format(self.id_no)
