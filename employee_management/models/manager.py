from models.employee import Employee


class Manager(Employee):

    def __init__(self, emp_id, name, age, email, base_salary):
        super().__init__(emp_id, name, age, email)
        self.base_salary = base_salary

    def calculate_salary(self):

        bonus = self.performance * 500000
        return self.base_salary + bonus