class Employee:
    def __init__(self, name, number):
        self.name = name
        self.number = number
    def get_name(self):
        return self.name
    def get_number(self):
        return self.number
    def set_name(self, name):
        self.name = name
    def set_number(self, number):
        self.number = number


class ProductionWorker(Employee):
    def __init__(self, name, number, shift, hourly_pay):
        super().__init__(name, number)
        self.shift = shift
        self.hourly_pay = hourly_pay
    def get_shift(self):
        return self.shift
    def get_hourly_pay(self):
        return self.hourly_pay
    def set_shift(self, shift):
        self.shift = shift
    def set_hourly_pay(self, hourly_pay):
        self.hourly_pay = hourly_pay


class ShiftSupervisor(Employee):
    def __init__(self, name, number, annual_salary, annual_bonus):
        super().__init__(name, number)
        self.annual_salary = annual_salary
        self.annual_bonus = annual_bonus
    def get_annual_salary(self):
        return self.annual_salary
    def get_annual_bonus(self):
        return self.annual_bonus
    def set_annual_salary(self, annual_salary):
        self.annual_salary = annual_salary
    def set_annual_bonus(self, annual_bonus):
        self.annual_bonus = annual_bonus


def main():
    print("Enter Production Worker's Information:")
    name = input("Name: ")
    number = input("Employee Number: ")
    shift = int(input("Shift (1 for day, 2 for night): "))
    hourly_pay = float(input("Hourly Pay: "))

    worker = ProductionWorker(name, number, shift, hourly_pay)

    print("\nEnter Shift Supervisor's Information:")
    name = input("Name: ")
    number = input("Employee Number: ")
    annual_salary = float(input("Annual Salary: "))
    annual_bonus = float(input("Annual Bonus: "))

    supervisor = ShiftSupervisor(name, number, annual_salary, annual_bonus)

    print("\nProduction Worker Information:")
    print(f"Name: {worker.get_name()}")
    print(f"Employee Number: {worker.get_number()}")
    print(f"Shift: {worker.get_shift()}")
    print(f"Hourly Pay: {worker.get_hourly_pay()}")

    print("\nShift Supervisor Information:")
    print(f"Name: {supervisor.get_name()}")
    print(f"Employee Number: {supervisor.get_number()}")
    print(f"Annual Salary: {supervisor.get_annual_salary()}")
    print(f"Annual Bonus: {supervisor.get_annual_bonus()}")


if __name__ == "__main__":
    main() 