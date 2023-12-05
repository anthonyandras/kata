from employees import Manager, Secretary, SalesPerson, FactoryWorker, TemporarySecretary
from productivity import ProductivitySystem
from contacts import Address


class PayrollSystem:
    def calculate_payroll(self, employees):
        print("Calculating payroll")
        print("-------")
        for employee in employees:
            print(f"payroll for: {employee.id} - {employee.name}")
            print(f"- Check Amount: {employee.calculate_payroll()}")
            if employee.address:
                print(f'- Sent to:')
                print(employee.address)
            print('')


if __name__ == '__main__':
    manager = Manager(1, "Duncan Andras", 1500)
    manager.address = Address(
        "123 Admin Road",
        "Chicago",
        "IL",
        60610
    )

    secretary = Secretary(2, "Dotty Andras", 1200)
    sales_guy = SalesPerson(3, "Peanut Andras", 1000, 250)
    factory_worker = FactoryWorker(4, "Anthony Andras", 40, 10)
    temporary_secretary = TemporarySecretary(5, 'Chibi Andras', 40, 9)

    payroll_system = PayrollSystem()
    payroll_system.calculate_payroll([
        manager, secretary, sales_guy, factory_worker, temporary_secretary
    ])

    # payroll_system = PayrollSystem()
    # payroll_system.calculate_payroll([
    #     salary_employee,
    #     hourly_employee,
    #     commission_employee
    # ])
