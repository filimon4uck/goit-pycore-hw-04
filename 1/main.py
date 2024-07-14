import pathlib
from statistics import mean


current_dir = pathlib.Path(__file__).parent


def total_salary(path):
    try:
        with open(path, mode="r", encoding="utf-8") as file:
            salaries = [int(salary.strip().split(',')[
                1]) for salary in file]
            return [sum(salaries), mean(salaries)]
    except FileNotFoundError:
        return 'File not found'


print(total_salary(current_dir/"file1.txt"))
