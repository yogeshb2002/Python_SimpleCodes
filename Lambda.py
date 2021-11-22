from functools import *                             #reduce() method imported.

int_list =[1, 2, 4, 6, 7, 8, 9, 12, 34, 56, 89, 77]

even_list = list(filter(lambda n : n%2 == 0, int_list))         #filters the list returning the evens only.
print(even_list)

square_evens = list(map(lambda n : n*n, even_list))         #take each evens and return the square of it.
print(square_evens)

final_sum = reduce(lambda a, b : a+b, square_evens)         #return the sum of square_evens list elements.
print(final_sum)