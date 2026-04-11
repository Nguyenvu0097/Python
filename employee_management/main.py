from models.manager import Manager
from models.developer import Developer
from models.intern import Intern

from services.company import Company
from services.payroll import *

from utils.validators import *

company = Company()


# ================= MENU HIỂN THỊ =================

def show_main_menu():

    print("\n" + "=" * 70)
    print("        HỆ THỐNG QUẢN LÝ NHÂN VIÊN CÔNG TY ABC")
    print("=" * 70)

    print("1. Thêm nhân viên mới")
    print("   a. Thêm Manager")
    print("   b. Thêm Developer")
    print("   c. Thêm Intern")

    print("2. Hiển thị danh sách nhân viên")
    print("   a. Tất cả nhân viên")
    print("   b. Theo loại")
    print("   c. Theo hiệu suất")

    print("3. Tìm kiếm nhân viên")
    print("   a. Theo ID")
    print("   b. Theo tên")

    print("4. Quản lý lương")
    print("   a. Lương từng nhân viên")
    print("   b. Tổng lương công ty")
    print("   c. Top 3 lương cao nhất")

    print("5. Quản lý dự án")
    print("   a. Phân công dự án")
    print("   b. Xóa dự án")
    print("   c. Hiển thị dự án")

    print("6. Đánh giá hiệu suất")
    print("   a. Cập nhật điểm")
    print("   b. Nhân viên xuất sắc")
    print("   c. Nhân viên cần cải thiện")

    print("7. Quản lý nhân sự")
    print("   a. Xóa nhân viên")
    print("   b. Tăng lương")
    print("   c. Thăng chức")
    print("   d. Cắt giảm nhân sự")

    print("8. Thống kê báo cáo")
    print("   a. Số lượng theo loại")
    print("   b. Tổng lương theo phòng")
    print("   c. Số dự án trung bình")

    print("9. Thoát")
    print("=" * 70)


# ================= THÊM NHÂN VIÊN =================

def add_manager():

    while True:

        try:

            emp_id = input("ID: ")
            name = input("Tên: ")

            age = int(input("Tuổi: "))
            validate_age(age)

            email = input("Email: ")
            validate_email(email)

            salary = float(
                input("Lương: ")
                .replace(".", "")
            )

            validate_salary(salary)

            emp = Manager(
                emp_id,
                name,
                age,
                email,
                salary
            )

            company.add_employee(emp)

            print("Đã thêm Manager!")
            break

        except ValueError:
            print("Sai định dạng!")

        except InvalidAgeError as e:
            print(e)

        except InvalidSalaryError as e:
            print(e)

        except DuplicateEmployeeError as e:
            print(e)


def add_developer():

    try:

        emp_id = input("ID: ")
        name = input("Tên: ")

        age = int(input("Tuổi: "))
        validate_age(age)

        email = input("Email: ")
        validate_email(email)

        salary = float(
            input("Lương cơ bản: ").replace(".", "")
        )

        overtime = int(
            input("Giờ tăng ca: ")
        )

        emp = Developer(
            emp_id,
            name,
            age,
            email,
            salary,
            overtime
        )

        company.add_employee(emp)

        print("Đã thêm Developer!")

    except Exception as e:
        print("Lỗi:", e)


def add_intern():

    try:

        emp_id = input("ID: ")
        name = input("Tên: ")

        age = int(input("Tuổi: "))
        validate_age(age)

        email = input("Email: ")
        validate_email(email)

        allowance = float(
            input("Trợ cấp: ").replace(".", "")
        )

        emp = Intern(
            emp_id,
            name,
            age,
            email,
            allowance
        )

        company.add_employee(emp)

        print("Đã thêm Intern!")

    except Exception as e:
        print("Lỗi:", e)


# ================= MENU CHÍNH =================

def main():

    while True:

        show_main_menu()

        choice = input("Chọn chức năng (1-9): ")

        # ===== MENU 1: THÊM NHÂN VIÊN =====

        if choice == "1":

            sub = input("Chọn (a,b,c): ")

            if sub == "a":
                add_manager()

            elif sub == "b":
                add_developer()

            elif sub == "c":
                add_intern()

        # ===== MENU 2: HIỂN THỊ =====

        elif choice == "2":

            sub = input("Chọn (a,b,c): ")

            if sub == "a":

                try:
                    company.list_employees()
                except Exception as e:
                    print(e)

            elif sub == "b":

                loai = input(
                    "Nhập loại (Manager/Developer/Intern): "
                )

                for e in company.employees:

                    if e.__class__.__name__ == loai:
                        e.display_info()

            elif sub == "c":

                emps = sorted(
                    company.employees,
                    key=lambda e: e.performance,
                    reverse=True
                )

                for e in emps:
                    e.display_info()

        # ===== MENU 3: TÌM KIẾM =====

        elif choice == "3":

            sub = input("Chọn (a,b,c): ")

            if sub == "a":

                emp_id = input("Nhập ID: ")

                try:

                    emp = company.find_employee(emp_id)
                    emp.display_info()

                except Exception as e:
                    print(e)

            elif sub == "b":

                name = input("Nhập tên: ")

                for e in company.employees:

                    if name.lower() in e.name.lower():
                        e.display_info()

        # ===== MENU 4: LƯƠNG =====

        elif choice == "4":

            sub = input("Chọn (a,b,c): ")

            if sub == "a":

                emp_id = input("Nhập ID: ")

                try:

                    emp = company.find_employee(emp_id)

                    salary = emp.calculate_salary()

                    print(
                        "Lương:",
                        f"{salary:,.0f}"
                    )

                except Exception as e:
                    print(e)

            elif sub == "b":

                total = calculate_total_salary(
                    company
                )

                print(
                    "Tổng lương:",
                    f"{total:,.0f}"
                )

            elif sub == "c":

                emps = sorted(
                    company.employees,
                    key=lambda e:
                    e.calculate_salary(),
                    reverse=True
                )

                print("Top 3 lương cao nhất:")

                for e in emps[:3]:
                    e.display_info()

        # ===== MENU 5: QUẢN LÝ DỰ ÁN =====

        elif choice == "5":

            sub = input("Chọn (a,b,c): ")

            if sub == "a":

                emp_id = input("ID: ")
                project = input("Tên dự án: ")

                try:

                    emp = company.find_employee(emp_id)
                    emp.assign_project(project)

                    print("Đã phân công!")

                except Exception as e:
                    print(e)

            elif sub == "b":

                emp_id = input("ID: ")
                project = input("Tên dự án: ")

                try:

                    emp = company.find_employee(emp_id)

                    if project in emp.projects:

                        emp.projects.remove(project)

                        print("Đã xóa dự án!")

                except Exception as e:
                    print(e)

            elif sub == "c":

                emp_id = input("ID: ")

                try:

                    emp = company.find_employee(emp_id)

                    print("Danh sách dự án:")

                    for p in emp.projects:
                        print("-", p)

                except Exception as e:
                    print(e)

        # ===== MENU 6: HIỆU SUẤT =====

        elif choice == "6":

            sub = input("Chọn (a,b,c): ")

            if sub == "a":

                emp_id = input("ID: ")

                try:

                    score = float(
                        input("Điểm (0-10): ")
                    )

                    emp = company.find_employee(emp_id)

                    emp.set_performance(score)

                    print("Đã cập nhật!")

                except Exception as e:
                    print(e)

            elif sub == "b":

                print("Nhân viên xuất sắc:")

                for e in company.employees:

                    if e.performance > 8:
                        e.display_info()

            elif sub == "c":

                print("Nhân viên cần cải thiện:")

                for e in company.employees:

                    if e.performance < 5:
                        e.display_info()

        # ===== MENU 7: NHÂN SỰ =====

        elif choice == "7":

            sub = input("Chọn (a,b,c,d): ")

            # Xóa nhân viên

            if sub == "a":

                emp_id = input("ID: ")

                try:

                    company.delete_employee(emp_id)

                except Exception as e:
                    print(e)

            # Tăng lương

            elif sub == "b":

                emp_id = input("ID: ")

                try:

                    amount = float(
                        input("Số tiền tăng: ")
                        .replace(".", "")
                    )

                    company.increase_salary(
                        emp_id,
                        amount
                    )

                except Exception as e:
                    print(e)

            # Thăng chức

            elif sub == "c":

                emp_id = input("ID: ")

                try:

                    company.promote_employee(emp_id)

                except Exception as e:
                    print(e)

            # Cắt giảm nhân sự

            elif sub == "d":

                try:

                    number = int(
                        input(
                            "Số nhân viên cần cắt giảm: "
                        )
                    )

                    company.layoff_employees(number)

                except Exception as e:
                    print(e)

        # ===== MENU 8: THỐNG KÊ =====

        elif choice == "8":

            sub = input("Chọn (a,b): ")

            if sub == "a":

                m = 0
                d = 0
                i = 0

                for e in company.employees:

                    if e.__class__.__name__ == "Manager":
                        m += 1

                    elif e.__class__.__name__ == "Developer":
                        d += 1

                    elif e.__class__.__name__ == "Intern":
                        i += 1

                print("Manager:", m)
                print("Developer:", d)
                print("Intern:", i)

            elif sub == "b":

                total = calculate_total_salary(
                    company
                )

                print(
                    "Tổng lương công ty:",
                    f"{total:,.0f}"
                )

        # ===== THOÁT =====

        elif choice == "9":

            print("Thoát chương trình...")
            break

        else:

            print("Chọn sai!")


if __name__ == "__main__":
    main()