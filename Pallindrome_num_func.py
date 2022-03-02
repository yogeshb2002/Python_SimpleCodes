def pallindrome(num):
    copy = num
    res = 0

    while num > 0:
        rem = num % 10        #clt the reminder
        res = res * 10 + rem  #result number
        num = num // 10       #number for nxt itrtion.
        
    if res == copy:
        print("Number is Pallindrome.")

    else:
        print("Number is not Pallindrome.")

num = int(input("Enter the number to Check : "))
pallindrome(num)