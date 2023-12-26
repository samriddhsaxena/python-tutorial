class Employee:
    company = "Google"
    def getSalary(self):
        print(f"Salary is {self.salary}")
    
    @staticmethod
    def greet():
        print("Good Morning, Sir")

    @staticmethod
    def time():
        print("The time is 9am in the morning.")

harry = Employee()
harry.salary = 10000
harry.greet()
harry.time()