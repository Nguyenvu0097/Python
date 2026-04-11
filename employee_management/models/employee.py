from abc import ABC, abstractmethod
from exceptions.employee_exceptions import (
    ProjectAllocationError
)


class Employee(ABC):

    def __init__(
            self,
            emp_id,
            name,
            age,
            email):

        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.email = email
        self.projects = []
        self.performance = 0

    # ===== PHÂN CÔNG DỰ ÁN =====

    def assign_project(self, project):

        if len(self.projects) >= 5:
            raise ProjectAllocationError(
                "Nhân viên đã đủ 5 dự án"
            )

        self.projects.append(project)

    # ===== ĐIỂM HIỆU SUẤT =====

    def set_performance(self, score):

        if score < 0 or score > 10:
            raise ValueError(
                "Điểm phải từ 0-10"
            )

        self.performance = score

    @abstractmethod
    def calculate_salary(self):
        pass

    def display_info(self):

        print(
            f"{self.emp_id} | "
            f"{self.name} | "
            f"{self.age} | "
            f"{self.email}"
        )