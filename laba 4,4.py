class Employee:
    # Метод класса для установки стандартной зарплаты
    @classmethod
    def set_default_salary(cls, salary):
        cls.default_salary = salary

    # Метод экземпляра для инициализации объекта Employee
    def __init__(self, name, position, salary=None):
        self.name = name
        self.position = position
        if salary is None:
            # Используем стандартную зарплату, если она не указана
            self.salary = self.default_salary
        else:
            self.salary = salary

    # Метод экземпляра для увеличения зарплаты на заданный процент
    def increase_salary(self, percent):
        self.salary += self.salary * percent / 100

    # Метод экземпляра для вывода информации о работнике
    def display_info(self):
        print("Имя: " + self.name)
        print("Должность: " + self.position)
        print("Зарплата: " + str(self.salary) + " рублей")

    # Статический метод для вычисления средней зарплаты из списка работников
    @staticmethod
    def calculate_average_salary(employees):
        total_salary = sum(employee.salary for employee in employees)
        average_salary = total_salary / len(employees)
        return average_salary

Employee.set_default_salary(50000)

employee1 = Employee("Иван", "Программист", 60000)
employee2 = Employee("Мария", "Дизайнер", 55000)
employee3 = Employee("Петр", "Менеджер")

employee3.increase_salary(10)

employee1.display_info()
print("-----------------------")
employee2.display_info()
print("-----------------------")
employee3.display_info()

# Создадим список работников и вычислим среднюю зарплату
employees_list = [employee1, employee2, employee3]
average_salary = Employee.calculate_average_salary(employees_list)
print("-----------------------")
print("Средняя зарплата в организации: " + str(average_salary) + " рублей")