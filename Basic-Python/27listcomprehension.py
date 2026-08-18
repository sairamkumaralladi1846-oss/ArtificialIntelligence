square_list = []

for i in range(6):
    square_list.append(i**2)
print(square_list)

sq_list = [ i**2 for  i in range(6)]
print(sq_list)

sq_odd_list = [ i**2 for i in range(6) if i%2 != 0]
print(sq_odd_list)

list_a = [-1,-3,3,23,-4,2,5,-2]
positive_list = [0 if i <0 else i for i in list_a]
print(positive_list)


list_c = ["apple", "banana", "cherry", "date", "fig", "grape"]

upper_list = [i.upper() for i in list_c]
print(upper_list)
