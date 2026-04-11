from models.employee import Employee


class Intern(Employee):

    def __init__(
            self,
            emp_id,
            name,
            age,
            email,
            allowance):

        super().__init__(
            emp_id,
            name,
            age,
            email)

        self.allowance = allowance

    def calculate_salary(self):

        return self.allowance