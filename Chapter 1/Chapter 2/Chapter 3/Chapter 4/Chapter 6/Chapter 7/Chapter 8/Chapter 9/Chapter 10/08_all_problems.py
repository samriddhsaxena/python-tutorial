#To create class programmer for storing info of few Mirosoft workers.

class Programmer:
    company = "Microsoft"
    def __init__(self,name,product):
        self.name = name
        self.product = product
    def getInfo(self):
        print(f"The name of the programmer is {self.name} and the product is {self.product}")

harry = Programmer("Harry","Skype")
Alka = Programmer("Alka","Github")
harry.getInfo()
Alka.getInfo()