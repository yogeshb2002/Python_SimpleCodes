class Daddy:

    def __init__(self, mobile):
        self.mobile = mobile

    def Mobile(self):
        print("I have my dad's {} mobile phone.".format(self.mobile))

class Son(Daddy):

    def __init__(self, mobile):
        super().__init__(mobile)

    def Mobile(self):
        print("I have my {} mobile phone.".format(self.mobile))

Varun = Son("Vivo")
Varun.Mobile()

#Here we have two methods with the same name in both classes.
#In the sub class we have overriden the method it will invoke the method of the sub cls.
#if the sub class dosen't have the method then super cls's method will be invoked.