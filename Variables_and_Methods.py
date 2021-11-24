class Company:

    Company_name = "Oritech"                #class variable remains same for all objects.

    def __init__(self, name, age, city, experience): #Variables inside the constructor are instance variables.
        self.name = name                          #Which can be modified.
        self.age = age
        self.city = city
        self.experience = experience

    def display(self):          #the method which deals with instance variable are instance methods.
        return "Hello, "+self.name+"\nYour details as follows:\nname : "+self.name+"\nage : "+self.age+"\ncity : "+self.city+"\nexperience : "+self.experience

    @classmethod            #the method which deals with class variables are class methods.
    def get_company(cls):
        return "Company name = "+cls.Company_name

    @staticmethod       #the method which do not bother about either class or instance variables.
    def message():
        return "Have a Great work day ...!"

Emp1 = Company("James", "23", "Banglore", "1 year")
Emp2 = Company("Arya", "25", "Mumbai", "3 years")

#Emp1 object accessing the methods of the class.
print(Emp1.display())
print(Emp1.get_company())
print(Emp1.message())

#Emp2 object accessing the methods of the class.
print(Emp2.display())
print(Emp2.get_company())
print(Emp2.message())