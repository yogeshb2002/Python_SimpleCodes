def MinMax(List):
    max = List[0]
    min = List[0]
    for ele in range(len(List)):
        if List[ele] < min:
            min = List[ele]
            
        if List[ele] > max:
            max = List[ele]
            
    return min, max

arr = []
length = int(input("Enter the length of the list : "))
print("Enter the elements : ")

for i in range(length):
    ele = int(input())
    arr.append(ele)
    
min, max = MinMax(arr)
print("Max = {} and Min = {}".format(max, min))
