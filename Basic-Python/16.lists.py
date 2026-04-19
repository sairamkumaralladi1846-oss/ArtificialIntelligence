# Problem Statement:
# Create a Student Marks Management System that performs the following:
# 1. Take comma-separated marks as input and convert to a list of integers.
# 2. Show basic list details (first mark, last 3, length).
# 3. Add marks using append(), insert(), and extend().
# 4. Remove marks using remove() and pop().
# 5. Sort ascending and descending.
# 6. Find max, min, and count occurrences of highest mark.
# 7. Check if a user-given mark exists in the list.
# 8. Create a "pass list" using list comprehension (marks ≥ 60).
# 9. Copy the list and convert final list to a string using join().
# 10. Store both lists in a nested list and print the final result.

# ---------------- Program Starts ----------------

# 1) Taking input marks as comma-separated values
marks = input("Enter marks separated by commas: ")

# 2) Convert to list of integers
marks_list = [int(x) for x in marks.split(",")]

print("\nOriginal Marks List:", marks_list)

# 3) Display basic info
print("First mark:", marks_list[0])
print("Last three marks:", marks_list[-3:])
print("Total number of marks:", len(marks_list))

# 4) Append new mark
new_mark = int(input("\nEnter a mark to append: "))
marks_list.append(new_mark)
print("After append:", marks_list)

# 5) Insert mark at a position
insert_mark = int(input("Enter another mark to insert: "))
pos = int(input("Enter position to insert at: "))
marks_list.insert(pos, insert_mark)
print("After insert:", marks_list)

# 6) Extend list
marks_list.extend([55, 98])
print("After extend:", marks_list)

# 7) Remove a mark by value + pop by index
remove_mark = int(input("\nEnter a mark to remove: "))
marks_list.remove(remove_mark)
print("After remove:", marks_list)

pop_index = int(input("Enter index to pop: "))
marks_list.pop(pop_index)
print("After pop:", marks_list)

# 8) Sorting
print("\nSorted ascending:", sorted(marks_list))
print("Sorted descending:", sorted(marks_list, reverse=True))

# 9) Statistical info
highest = max(marks_list)
lowest = min(marks_list)
print("\nHighest mark:", highest)
print("Lowest mark:", lowest)
print("Occurrences of highest mark:", marks_list.count(highest))

# 10) Membership check
search_mark = int(input("\nEnter a mark to search: "))
print("Exists?" , search_mark in marks_list)

# 11) Pass list using list comprehension
pass_list = [m for m in marks_list if m >= 60]
print("\nPass List:", pass_list)

# 12) Copy list
copied_list = marks_list.copy()
print("Copied List:", copied_list)

# 13) Convert to string using join()
marks_str = " - ".join(str(m) for m in marks_list)
print("\nFinal List as String:", marks_str)

# 14) Nested list
nested = [marks_list, pass_list]
print("\nNested List:", nested)


# ---------------- Sample Inputs & Outputs ----------------

'''
Sample Input:
Enter marks separated by commas: 87,45,66,92
Enter a mark to append: 73
Enter another mark to insert: 50
Enter position to insert at: 1
Enter a mark to remove: 45
Enter index to pop: 2
Enter a mark to search: 92

Sample Output:
Original Marks List: [87,45,66,92]
First mark: 87
Last three marks: [45,66,92]
Total number of marks: 4

After append: [87,45,66,92,73]
After insert: [87,50,45,66,92,73]
After extend: [87,50,45,66,92,73,55,98]
After remove: [87,50,66,92,73,55,98]
After pop: [87,50,92,73,55,98]

Sorted ascending: [50,55,73,87,92,98]
Sorted descending: [98,92,87,73,55,50]

Highest mark: 98
Lowest mark: 50
Occurrences of highest mark: 1

Exists? True

Pass List: [87,92,73,98]
Copied List: [87,50,92,73,55,98]

Final List as String: 87 - 50 - 92 - 73 - 55 - 98

Nested List: [[87,50,92,73,55,98],[87,92,73,98]]
'''
