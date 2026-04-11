from models.employee import Employee


class Developer(Employee):

    def __init__(
            self,
            emp_id,
            name,
            age,
            email,
            base_salary,
            overtime):

        super().__init__(
            emp_id,
            name,
            age,
            email)

        self.base_salary = base_salary
        self.overtime = overtime

    def calculate_salary(self):

        overtime_pay = self.overtime * 200000
        return self.base_salary + overtime_pay