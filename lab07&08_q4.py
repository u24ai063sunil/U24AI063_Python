class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __add__(self, other):
        if isinstance(other, Employee):
            return Employee(f"{self.name} & {other.name}", self.salary + other.salary)
        else:
            raise TypeError("Operand must be an Employee object.")

    def __sub__(self, other):
        if isinstance(other, Employee):
            return self.salary - other.salary
        else:
            raise TypeError("Operand must be an Employee object.")

    def __str__(self):
        
        return f"{self.name}: ${self.salary}"

    def __repr__(self):
        return f"Employee('{self.name}', {self.salary})"

    def __eq__(self, other):
        if isinstance(other, Employee):
            return self.salary == other.salary
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        if isinstance(other, Employee):
            return self.salary < other.salary
        else:
            raise TypeError("Operand must be an Employee object.")

    def __le__(self, other):
        if isinstance(other, Employee):
            return self.salary <= other.salary
        else:
            raise TypeError("Operand must be an Employee object.")

    def __gt__(self, other):
        if isinstance(other, Employee):
            return self.salary > other.salary
        else:
            raise TypeError("Operand must be an Employee object.")

    def __ge__(self, other):
        if isinstance(other, Employee):
            return self.salary >= other.salary
        else:
            raise TypeError("Operand must be an Employee object.")



employee1 = Employee("sunil", 60000)
employee2 = Employee("vikram", 75000)
employee3 = Employee("pramod", 60000)

combined_salary = employee1 + employee2
print(f"Combined Salary: {combined_salary}")

salary_difference = employee2 - employee1
print(f"Salary Difference (vikram - sunil): ${salary_difference}")

print(f"sunil == vikram: {employee1 == employee2}")
print(f"sunil == vikram: {employee1 == employee3}")
print(f"sunil != vikram: {employee1 != employee2}")
print(f"sunil < vikram: {employee1 < employee2}")
print(f"sunil <= pramod: {employee1 <= employee3}")
print(f"vikram > pramod: {employee2 > employee1}")
print(f"vikram >= pramod: {employee2 >= employee3}")
