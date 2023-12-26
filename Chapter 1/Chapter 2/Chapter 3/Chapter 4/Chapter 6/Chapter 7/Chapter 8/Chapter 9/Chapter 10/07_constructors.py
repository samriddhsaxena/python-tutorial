class Employee:
    company = "Google"
    
    def __init__(self):
        print("Employee is created.")

    def getSalary(self):
        print(f"Salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good Morning, Sir")

    @staticmethod
    def time():
        print("The time is 9am in the morning.")

harry = Employee()