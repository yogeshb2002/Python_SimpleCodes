#Problem : Spiral Traversal of Matrix
list1 = [[3, 4, 5, 6],
         [7, 8, 9, 10],
         [11, 12, 13, 14],
         [15, 16, 11, 12],
         [3, 4, 5, 2]]

top = 0
bottom = len(list1)-1
righ = 0 
left = len(list1[0])-1
result = []

while righ <= left and top <= bottom:
    #add the elements of the first row
    for i in range(righ, left+1):
        result.append(list1[top][i])
    top +=1
    #add the elements of the last column
    for i in range(top, bottom+1):
        result.append(list1[i][left])
    left -=1
    #add the elements of the remaining rows
    if top <= bottom:
        for i in range(left, righ-1, -1):
            result.append(list1[bottom][i])
        bottom -=1
    #add the elements of the remaining columns
    if righ <= left:
        for i in range(bottom, top-1, -1):
            result.append(list1[i][righ])
        righ += 1
   
print("Spiral Traversal of Matrix : ", result)
