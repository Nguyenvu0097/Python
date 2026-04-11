from exceptions.employee_exceptions import (
    EmployeeNotFoundError,
    DuplicateEmployeeError
)


class Company:

    def __init__(self):

        self.employees = []

    # ===== THÊM NHÂN VIÊN =====

    def add_employee(self, emp):

        for e in self.employees:

            if e.emp_id == emp.emp_id:

                # Tự động sinh ID mới
                new_id = emp.emp_id + "_new"

                emp.emp_id = new_id

                raise DuplicateEmployeeError(
                    f"ID trùng! Đã đổi thành {new_id}"
                )

        self.employees.append(emp)

    # ===== HIỂN THỊ =====

    def list_employees(self):

        if not self.employees:
            raise IndexError(
                "Chưa có dữ liệu"
            )

        for e in self.employees:
            e.display_info()

    # ===== TÌM =====

    def find_employee(self, emp_id):

        for e in self.employees:

            if e.emp_id == emp_id:
                return e

        raise EmployeeNotFoundError(emp_id)

    # ===== XÓA =====

    def delete_employee(self, emp_id):

        emp = self.find_employee(emp_id)
        self.employees.remove(emp)