class PersonData:           #outer class.

    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city
        
    def giveData(self):
        print("Name = {}\nAge = {}\nCity = {}".format(self.name, self.age, self.city))
        
    class BankDetails:          #inner class or Nested class.

        def __init__(self, BankName, AccNo, BranchCode):
            self.BankName = BankName
            self.AccNo = AccNo
            self.BranchCode = BranchCode

        def giveData(self):
            print("\t\t\t-----Your Bank details----\n ")
            print("Bank : {}\nAccount Number : {}\nBranch Code : {}".format(self.BankName, self.AccNo, self.BranchCode))

Arun = PersonData("Arun", 34, "Banglore")
Arun.giveData()
Arun = Arun.BankDetails("SBI", 756835683, 87509) #created the object of inner class using the object of outer class.
Arun.giveData()
print(id(Arun))