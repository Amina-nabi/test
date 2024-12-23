class Technician(Employee):
    def __init__(self, name=" ", employee=" ", specilization=" "):
        super().__init__(name, employee_id)
        self.specilization = specilization

    def perform_maintenance(self):
        return f"{self.name} выполняет техническое обслуживание по специальности {self.specilization}"


class TechManager(Manager, Technician):
    def __init__(self, name, employee_id, department, specialization):
        super().__init__(name, employee_id, department)
        super().__init__(name, employee_id, specialization)
        self.team = []

    def add_emploeyee(self, employee):
        self.team.append(employee)
