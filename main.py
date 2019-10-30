class Employee:
    raise_amt = 1.04

    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.email = first_name + '.' + last_name + '@company.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def __add__(self, other):
        return self.pay + other.pay


emp_1 = Employee('Wasim', 'Rana', 50000)
emp_2 = Employee('David', 'Smith', 70000)

# print(emp_1 + emp_2)
# print('Wasim'.__len__())

print(emp_1.fullname())


class Employee:
    # class instance
    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
        self.email = fname + '_' + lname + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.fname, self.lname)

    def salary_info(self):
        return "{} {}'s salary is {}".format(self.fname, self.lname, self.salary)


emp_1 = Employee('Wasim', 'Rana', 5000)
emp_2 = Employee('David', 'Smith', 7000)

print(emp_1.fullname())
print(emp_1.salary_info())
print(emp_1.email)
print('================')
print(emp_2.fullname())
print(emp_2.salary_info())
print(emp_2.email)
