from abc import ABC, abstractmethod #importing the method, class to use abstract class
class Programer1:
    
    @abstractmethod     #abstract method
    def coding(self):
        pass

class Programer2(Programer1):

    def coding(self):                   #defing the method
        print("Writing the code...")

Arun = Programer2()
Arun.coding()
print("Hello")