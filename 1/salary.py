
from statistics import mean


def total_salary(path):
    try:
        with open(file=path, mode="r", encoding="utf-8") as file:
            salaries = [int(salary.strip().split(',')[
                1]) for salary in file if salary.strip().split(',')[1].strip().isdigit()]
            return [sum(salaries), mean(salaries) if len(salaries) > 0 else 0]
    except FileNotFoundError:
        return "File not found"
