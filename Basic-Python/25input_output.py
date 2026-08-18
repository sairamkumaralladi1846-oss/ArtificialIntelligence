# -- start of file i/o concepts --

f = open("sample.txt", 'r')
# print(f.read())
# print(f.readline())
# print(f.readlines())
f.close()

# sample text file 
# for i/o concepts learning
# this is first file


#--- writing to a file ---
# f = open("sample.txt", 'w')
# f.write ("This writes to the file. This will overwrite existing content.")
# f.close() 

# # --- appending to a file ---
# f = open("sample.txt", 'a')
# f.write("\nThis line is appended to the file.")
# f.close()

# # --- Using r+ mode reading and writing ---
# f = open("sample.txt", 'r+')
# print(f.read())
# f.write("\nThis line is added using r+ mode. after reading the file.")
# f.close()

# # --- Using r+ mode writing and reading ---
# f = open("sample.txt", 'r+')
# f.write("r+ mode.")
# print(f.read())
# f.write("r+ mode.")
# print(f.read())
# f.close()

# --- Using w+ mode writing and reading ---
# f = open("sample.txt", 'w+')
# f.write("w+ mode.")
# f.seek(0)  # Move the file pointer to the beginning of the file
# print(f.read())
# f.write("\nThis line is added using w+ mode. after reading the file.")
# f.seek(0)  # Move the file pointer to the beginning of the file
# print(f.read())
# f.close()

# -- using a+ mode for appending and reading ---
# f = open("sample.txt", 'a+')
# f.write("\nThis line is added using a+ mode. after reading the file.")
# f.seek(0)  # Move the file pointer to the beginning of the file
# print(f.read())
# f.close() 

# -- using with statement for file handling ---
# with open("sample.txt", 'r') as f:
#     print(f.read())

