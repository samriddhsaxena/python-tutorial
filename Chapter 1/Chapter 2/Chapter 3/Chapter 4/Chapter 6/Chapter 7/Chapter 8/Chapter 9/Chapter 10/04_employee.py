# from curses.ascii import EM


class Employee:
    company = "Google"

harry = Employee()
rajni = Employee()

print(harry.company)
print(rajni.company)

Employee.company = "YouTube"
print(harry.company)
print(rajni.company)
