class Employee:
    def __init__(self, name = " ", employee_id = " "):
        self.name = name
        self.employee_id = employee_id

    def get_info(self):
        return f"Имя: {self.name}, ID: {self.employee_id}"


class Manager(Employee):
    def __init__(self, name = " ", employee_id = " ", depatment = " "):
        super(). __init__(name, employee_id)
        self.depatment = depatment

    def manage_project(self):
        return f"{self.name} управляет проектом в отделе {self.depatment}"



