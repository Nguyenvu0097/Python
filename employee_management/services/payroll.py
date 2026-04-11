def calculate_total_salary(company):

    total = 0

    for emp in company.employees:
        total += emp.calculate_salary()

    return total


def highest_salary(company):

    if not company.employees:
        return None

    return max(
        company.employees,
        key=lambda e: e.calculate_salary()
    )