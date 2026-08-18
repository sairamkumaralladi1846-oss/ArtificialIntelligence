# Problem Statement:
# Create an Employee Data Management Program using tuples. Perform the following tasks:
#
# 1. Take a comma-separated input of employee names and store them in a tuple.
# 2. Display:
#    - First employee
#    - Last two employees
#    - Total number of employees
# 3. Ask user for an employee name and check if it exists in the tuple.
# 4. Count how many times a user-given name appears.
# 5. Convert the tuple to a list and allow adding a new employee name.
# 6. Sort the list alphabetically and convert it back to a tuple.
# 7. Ask for an employee name and remove it if found (after converting to list).
# 8. Use tuple unpacking to print the first three employee names (if available).
# 9. Create a tuple of tuples where each employee has an ID (starting from 1).
# 10. Print the final structured tuple.

# --------------------- Program Starts ---------------------

# 1) Taking employee names as comma-separated input
employees = input("Enter employee names, separated by commas: ")

# 2) Convert input to a tuple
emp_tuple = tuple(employees.split(","))

print("\nOriginal Tuple:", emp_tuple)

# 3) Display basic tuple information
print("First employee:", emp_tuple[0])
print("Last two employees:", emp_tuple[-2:])
print("Total employees:", len(emp_tuple))

# 4) Search employee
search_name = input("\nEnter a name to search: ")
print("Exists?", search_name in emp_tuple)

# 5) Counting occurrences
count_name = input("Enter a name to count: ")
print("Count:", emp_tuple.count(count_name))

# 6) Convert tuple → list to modify
emp_list = list(emp_tuple)

# Add a new name
new_name = input("\nEnter a new employee name to add: ")
emp_list.append(new_name)

# Sort employees and convert back to tuple
emp_list.sort()
emp_tuple = tuple(emp_list)
print("\nAfter adding & sorting:", emp_tuple)

# 7) Remove an employee (if present)
remove_name = input("\nEnter a name to remove: ")
if remove_name in emp_list:
    emp_list.remove(remove_name)
    emp_tuple = tuple(emp_list)
    print("After removal:", emp_tuple)
else:
    print("Name not found — no removal.")

# 8) Tuple unpacking demonstration
print("\nTuple Unpacking Example:")
if len(emp_tuple) >= 3:
    a, b, c, *others = emp_tuple
    print("First three names:", a, b, c)
else:
    print("Not enough employees for unpacking example.")

# 9) Create tuple of tuples with employee IDs
final_tuple = tuple((i + 1, emp_tuple[i]) for i in range(len(emp_tuple)))

# 10) Display final structured result
print("\nFinal Employee Data (ID, Name):")
print(final_tuple)


# ---------------- Sample Input & Output ----------------

'''
Sample Input:
Enter employee names, separated by commas: John,Alex,Sara,Mike,Sara
Enter a name to search: Sara
Enter a name to count: Sara
Enter a new employee name to add: David
Enter a name to remove: Mike

Sample Output:
Original Tuple: ('John', 'Alex', 'Sara', 'Mike', 'Sara')
First employee: John
Last two employees: ('Mike', 'Sara')
Total employees: 5

Exists? True
Count: 2

After adding & sorting: ('Alex', 'David', 'John', 'Mike', 'Sara', 'Sara')

After removal: ('Alex', 'David', 'John', 'Sara', 'Sara')

Tuple Unpacking Example:
First three names: Alex David John

Final Employee Data (ID, Name):
((1, 'Alex'), (2, 'David'), (3, 'John'), (4, 'Sara'), (5, 'Sara'))
'''
