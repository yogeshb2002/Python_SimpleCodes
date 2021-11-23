class Company:

    def __init__(self, name, age, city, experience): #Constructor in python, it is a special method.
        self.name = name                            # delcaring the attributes of the objects of class.
        self.age = age
        self.city = city
        self.experience = experience

    def display(self):
        print("Hello, "+self.name+"\nYour details as follows:\nname : "+self.name+"\nage : "+self.age+"\ncity : "+self.city+"\nexperience : "+self.experience )

#object creation of the class company.

Emply1 = Company("John", "25", "Banglore", "3 years")
Emply1.display()            #invoking the display method using object.