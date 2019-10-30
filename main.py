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
