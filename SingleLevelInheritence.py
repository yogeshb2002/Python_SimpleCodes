class Mammal:       #super class.

    def __init__(self, BloodColor, HeartChambers, Eyes):
        self.BloodColor = BloodColor
        self.HeartChambers = HeartChambers
        self.Eyes = Eyes

    def present1(self):
        print("\t\t\t\t--------Mammals Features---------\n")
        print("Blood Color : {}\nHeart chambers : {}\nEyes : {}\n".format(self.BloodColor, self.HeartChambers, self.Eyes))

class Human(Mammal):        #sub class inherited the super class.

    def __init__(self, BrainCapacity):
        super().__init__("Red", 4, 2)                #invoked the super class constructor because , if the sub class has
        self.BrainCapacity = BrainCapacity  # a constructor the super class constructor will not inherited by default.

    def present2(self):
        print("Brain Capacity = ",self.BrainCapacity)

Men = Human("1500 cc")  #created the object of sub class not the super class.
Men.present1()
Men.present2()

