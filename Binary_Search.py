def Binary(list, key, first, last):
    mid = 0
    if(first<last):
        mid = (first+last)//2
        if(key==list[mid]):
            print("postion = {} and key = {}".format(mid, key))
        elif(key>mid):
            Binary(list, key, mid+1, last)
        else:
            Binary(list, key, first, mid-1)

list = []
list_length = int(input("Enter the length of the list : "))
print("Enter the list elements :")
for iter in range(list_length):
    element = int(input())
    list.append(element)
print("List :", list) 

key = int(input("Enter the key to search : "))
low = 0
high = len(list) - 1

Binary(list, key, low, high )

    
    

