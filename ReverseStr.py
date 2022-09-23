String = ['h', 'e', 'l', 'l', 'o']
Rev_Str = []
length = len(String)

for i in range(length-1, 0-1, -1):
    Rev_Str.append(String[i])  #reversing and adding element to new list.
print("Reverse of given String: ", Rev_Str)

if String == Rev_Str: #check the pallindrome condition.
    print("The Given String is Pallindrome...")
else:
    print("The String is not a Pallindrome...")

    