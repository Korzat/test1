# class Employee:
#     def __init__(self, salary):
#         self._salary = salary
#     def set_salary(self, salary):
#         self._salary = salary
#         return f'Ваша зарплата сменена {self._salary}'

#     def get_salary(self):
#         return self._salary
#     def calculate_bonus(self):
#         pass


# class Developer(Employee):
#     def __init__(self, salary):
#         super().__init__(salary)
#     def calculate_bonus(self):
#         self._salary = self._salary * 1.1
#         return self._salary
#     def print_employee_info(self):
#         return f'Ваш бонус: 10%, ваша зарплата с бонусом: {self._salary}'

# class Manager(Employee):
#     def __init__(self, salary):
#         super().__init__(salary)
#     def calculate_bonus(self):
#         self.__salary= self.__salary *1.2
#         return self.__salary
#     def print_employee_info(self):
#         return f'Ваш бонус: 20%, ваша зарплата с бонусом: {self.__salary}'
# employee = Employee(12311)
# developer = Developer(20000)
# manager = Manager(10000)

# print(developer.calculate_bonus())
# print(developer.print_employee_info())



class Car:
    def __init__(self):
        pass
    @staticmethod
    def drive(speed):
        return f'Машина едет со скоростью {speed}'
print(Car.drive(12312))
