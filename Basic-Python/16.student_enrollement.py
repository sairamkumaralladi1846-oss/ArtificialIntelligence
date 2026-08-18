#Student Enrollement 
''' 
Given a list of tuples with info(name,subject):
1)list all unique courses
2)list all students enrolled in English
3)Create dictionary(student,set of cources)

Sample Input:
[("Alice","Math"), ("Bob","English"), ("Alice","English"), ("Charlie","Math"), ("Bob","Math")]

'''

enrollement = [("Alice","Math"), ("Bob","English"), ("Alice","English"), ("Charlie","Math"), ("Bob","Math")]

# 1) List unique courses
unique_courses = list(set(course for name,course in enrollement))
print(unique_courses)

# 2) List students enrolled in English
english_course_students = [name for name,course in enrollement if course=="English"]
print(english_course_students)

# 3) Create dictionary(student, set of courses)
dict = {}
for name,course in enrollement:
    if name in dict:
        dict[name].add(course)
    else:
        dict[name] = {course}
print(dict)
