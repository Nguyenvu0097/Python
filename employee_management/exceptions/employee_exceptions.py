class EmployeeException(Exception):
    """Base exception"""
    pass


class EmployeeNotFoundError(EmployeeException):

    def __init__(self, emp_id):
        self.emp_id = emp_id
        super().__init__(
            f"Không tìm thấy nhân viên có ID: {emp_id}"
        )


class InvalidSalaryError(EmployeeException):
    """Lương <= 0"""
    pass


class InvalidAgeError(EmployeeException):
    """Tuổi <18 hoặc >65"""
    pass


class ProjectAllocationError(EmployeeException):
    """Quá 5 dự án"""
    pass


class DuplicateEmployeeError(EmployeeException):
    """Trùng ID"""
    pass