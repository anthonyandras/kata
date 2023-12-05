from abc import ABC, abstractmethod

"""
An amazing example of a diamond problem using multiple inheritance - don't do this
in real code
"""


class Employee(ABC):
    """Abstract class for employee"""

    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.address = None

    @abstractmethod
    def calculate_payroll(self):
        """implementation of an abstract method"""
        pass

    @abstractmethod
    def work(self):
        pass


class SalaryEmployee(Employee):
    def __init__(self, id, name, weekly_salary):
        super().__init__(id, name)
        self._weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self._weekly_salary


class HourlyEmployee(Employee):
    def __init__(self, id, name, hours_worked, hour_rate):
        super().__init__(id, name)
        self._hours_worked = hours_worked
        self._hour_rate = hour_rate

    def calculate_payroll(self):
        return self._hour_rate * self._hours_worked


class CommissionEmployee(SalaryEmployee):
    def __init__(self, id, name, weekly_salary, commission):
        super().__init__(id, name, weekly_salary)
        self._commission = commission

    def calculate_payroll(self):
        return super().calculate_payroll() + self._commission


class Manager(SalaryEmployee):
    def work(self, hours):
        print(f"{self.name} screams and yells for {hours} hours.")


class Secretary(SalaryEmployee):
    def work(self, hours):
        print(f"{self.name} expends {hours} hours doing office paperwork.")


class SalesPerson(CommissionEmployee):
    def work(self, hours):
        print(f"{self.name} expends {hours} hours on the phone.")


class FactoryWorker(HourlyEmployee):
    def work(self, hours):
        print(f"{self.name} manufactures gadgets for {hours} hours.")


class TemporarySecretary(Secretary, HourlyEmployee):
    """Can figure out what is going on via the MRO - method resolution order
    When super() is detected, the next class is searched, _not_ the parent
    Algorithm: C3 Linearization
    """

    def __init__(self, id, name, hours_worked, hour_rate):
        HourlyEmployee.__init__(self, id, name, hours_worked, hour_rate)  # bypass the MRO

    def calculate_payroll(self):
        return HourlyEmployee.calculate_payroll(self)
