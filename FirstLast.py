
arr = [1, 2, 2, 2, 2, 3, 4, 5, 6, 7]
n = len(arr)
element = 2
first = -1
last = -1

for ele in range(0, n):
    if element != arr[ele]:
        continue
    if first == -1:
        first = ele
    last = ele
    
print("First position =", first, "and Last position =", last)


