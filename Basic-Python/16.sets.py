# Problem Statement:
# Create a Student Subject Selection System using sets. Perform the following:
#
# 1. Take two sets as input:
#       - Available subjects
#       - Subjects selected by a student
# 2. Display:
#       - Number of available subjects
#       - Number of selected subjects
# 3. Check if selected subjects are valid (subset of available subjects).
# 4. Add a new subject to the available subjects using add().
# 5. Remove a subject using remove() and discard() (show difference).
# 6. Find:
#       - Subjects student did NOT choose (difference)
#       - Common subjects with another student (intersection)
#       - All subjects chosen by both students (union)
# 7. Check if two students selected exactly same subjects.
# 8. Convert the set to frozen set.
# 9. Print the final sets.

# ------------------ Program Starts ------------------

# 1) Take input for available subjects
available = set(input("Enter available subjects (comma separated): ").split(","))

# Take student selection input
student1 = set(input("Enter subjects selected by student-1: ").split(","))

print("\nAvailable subjects:", available)
print("Student-1 selected:", student1)

# 2) Display sizes
print("\nTotal available subjects:", len(available))
print("Subjects selected by student-1:", len(student1))

# 3) Check if valid subset
print("\nAre selected subjects valid?", student1.issubset(available))

# 4) Add a new subject
new_sub = input("\nEnter a new subject to add: ")
available.add(new_sub)
print("After adding:", available)

# 5) Removing subjects
remove_sub = input("\nEnter a subject to remove: ")

# using remove() - throws error if not present
if remove_sub in available:
    available.remove(remove_sub)
else:
    print(f"{remove_sub} not found, skipping remove()")

# using discard() - no error if not present
discard_sub = input("Enter another subject to discard: ")
available.discard(discard_sub)

print("After removal operations:", available)

# 6) Second student input for set operations
student2 = set(input("\nEnter subjects selected by student-2: ").split(","))

print("\nStudent-2 selected:", student2)

# Union, intersection, difference
print("Common subjects:", student1.intersection(student2))
print("All chosen subjects:", student1.union(student2))
print("Subjects chosen by Student-1 but not Student-2:", student1.difference(student2))

# 7) Check equality
print("\nDid both students choose the same subjects?", student1 == student2)

# 8) Convert to frozen set
frozen_available = frozenset(available)
print("\nFrozen available subjects:", frozen_available)

# 9) Final display
print("\nFinal Sets:")
print("Available:", available)
print("Student-1:", student1)
print("Student-2:", student2)


# ---------------- SAMPLE INPUT & OUTPUT ----------------

'''
Sample Input:
Enter available subjects (comma separated): Math,Physics,Chemistry,Biology,English
Enter subjects selected by student-1: Math,Physics
Enter a new subject to add: CS
Enter a subject to remove: Biology
Enter another subject to discard: Hindi
Enter subjects selected by student-2: Physics,Chemistry,Math

Sample Output:
Available subjects: {'Math','Physics','Chemistry','Biology','English'}
Student-1 selected: {'Math','Physics'}

Total available subjects: 5
Subjects selected by student-1: 2

Are selected subjects valid? True

After adding: {'Math','Physics','Chemistry','Biology','English','CS'}
After removal operations: {'Math','Physics','Chemistry','English','CS'}

Student-2 selected: {'Math','Physics','Chemistry'}

Common subjects: {'Math','Physics'}
All chosen subjects: {'Math','Physics','Chemistry'}
Subjects chosen by Student-1 but not Student-2: set()

Did both students choose the same subjects? False

Frozen available subjects: frozenset({'Math','Physics','Chemistry','English','CS'})

Final Sets:
Available: {'Math','Physics','Chemistry','English','CS'}
Student-1: {'Math','Physics'}
Student-2: {'Math','Physics','Chemistry'}
'''
