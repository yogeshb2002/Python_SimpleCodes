class Grocery:

    def __init__(self, rice, sugar, vegetables):
        self.rice = rice
        self.sugar = sugar
        self.vegetables = vegetables

    def __add__(self, Second):              #defining the + operator in the present class.
        total1 = self.rice+self.sugar+self.vegetables
        total2 = Second.rice+Second.sugar+Second.vegetables
        return "Total cost you spent is {}".format(total1+total2)

    def __gt__(self, Second):               #defining the > operator in the present class.
        total1 = self.rice+self.sugar+self.vegetables
        total2 = Second.rice+Second.sugar+Second.vegetables
        if total1 > total2:
            return True
        else:
            return False
    
    def __str__(self):      #defining the print statement to print the objects of the class.
        return "Rice = {}, Sugar = {}, Vegetables = {}".format(self.rice, self.sugar, self.vegetables)
        
print("\t\t\t\t_________ YOUR GROCERY SHOPPING DETAILS _________")
shop1 = Grocery(30, 59, 20)
shop2 = Grocery(38,47,21)

print("Shop1 :",shop1)
print("Shop2 :",shop2)

total = shop1 + shop2
print(total)

if shop1 > shop2:
    print("Go to Shop2!")
else:
    print("Go to Shop1")