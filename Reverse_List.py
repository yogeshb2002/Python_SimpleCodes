def Reverse(List):
    #Reversing the list using list slicing.
    List = List[::-1]
    return List

num = []

length = int(input("Enter the length of the list : "))
for ele in range(length):
    num.append(ele)
     
print("Actual list : ", num)
print("Reversed list : ", Reverse(num))

#Reverse elements using reverse()
print("Reversed list : ", num.reverse())
    