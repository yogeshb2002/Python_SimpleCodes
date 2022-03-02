num = int(input("Enter the Number to check : "))
copy = num
res = 0

while num > 0:
    rem = num % 10       #clt the reminder
    res = res * 10 + rem  #result number
    num = num // 10       #number for nxt itrtion

if res == copy:
    print("Number is pallindrome.")

else:
    print("Number is not Pallindrome.")

