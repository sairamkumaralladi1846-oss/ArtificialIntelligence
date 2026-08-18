# Problem Statement:
# Create a Student Database System using dictionaries. Perform the following tasks:
#
# 1. Take student records as input in the format: name:marks (comma separated)
#    Example → "John:89, Sara:92, Mike:76"
# 2. Convert input into a dictionary.
# 3. Display:
#       - All keys (student names)
#       - All values (marks)
#       - Total number of students
# 4. Add a new student record.
# 5. Update marks of an existing student using update().
# 6. Remove a student using pop().
# 7. Check whether a student exists using "in".
# 8. Print:
#       - Student with highest marks
#       - Student with lowest marks
#       - Average marks
# 9. Create a new dictionary containing only passed students (marks ≥ 50).
# 10. Convert dictionary keys to a list and sort alphabetically.
# 11. Convert final dictionary into a list of tuples and print.

# -------------------- Program Starts --------------------

# 1) Taking comma-separated input
data = input("Enter student name and marks (Format: Name:Marks,Name:Marks): ")

# 2) Convert to dictionary
students = dict(item.split(":") for item in data.split(","))

# Convert string marks to int
students = {name: int(marks) for name, marks in students.items()}

print("\nStudent Dictionary:", students)

# 3) Display details
print("\nStudent Names:", list(students.keys()))
print("Marks:", list(students.values()))
print("Total Students:", len(students))

# 4) Add a new record
new_name = input("\nEnter new student name: ")
new_marks = int(input("Enter marks: "))
students[new_name] = new_marks
print("After adding:", students)

# 5) Update existing student
update_name = input("\nEnter student name to update marks: ")
if update_name in students:
    new_score = int(input("Enter updated marks: "))
    students.update({update_name: new_score})
    print("After updating:", students)
else:
    print(update_name, "not found!")

# 6) Remove a student using pop()
remove_name = input("\nEnter student name to remove: ")
removed = students.pop(remove_name, "Not Found")
print("After removal:", students)

# 7) Check student presence
search_name = input("\nEnter a name to search: ")
print("Exists?", search_name in students)

# 8) Highest, lowest, average marks
highest_student = max(students, key=students.get)
lowest_student = min(students, key=students.get)
average = sum(students.values()) / len(students)

print("\nTopper:", highest_student, "-", students[highest_student])
print("Lowest scorer:", lowest_student, "-", students[lowest_student])
print("Average marks:", average)

# 9) Pass dictionary (marks >= 50)
passed = {name: score for name, score in students.items() if score >= 50}
print("\nPassed Students:", passed)

# 10) Sorted keys list
sorted_names = sorted(students.keys())
print("Alphabetically Sorted Students:", sorted_names)

# 11) Convert dictionary to list of tuples
tuple_list = list(students.items())
print("\nDictionary as Tuple List:", tuple_list)


# -------------------- Sample Input & Output --------------------

'''
Sample Input:
Enter student name and marks: John:89,Sara:92,Mike:40

Enter new student name: David
Enter marks: 75

Enter student name to update marks: Mike
Enter updated marks: 55

Enter student name to remove: Sara

Enter a name to search: David


Sample Output:
Student Dictionary: {'John': 89, 'Sara': 92, 'Mike': 40}

After adding: {'John': 89, 'Sara': 92, 'Mike': 40, 'David': 75}
After updating: {'John': 89, 'Sara': 92, 'Mike': 55, 'David': 75}
After removal: {'John': 89, 'Mike': 55, 'David': 75}

Exists? True

Topper: John - 89
Lowest scorer: Mike - 55
Average marks: 73.0

Passed Students: {'John': 89, 'Mike': 55, 'David': 75}

Alphabetically Sorted Students: ['David', 'John', 'Mike']

Dictionary as Tuple List: [('John', 89), ('Mike', 55), ('David', 75)]
'''
