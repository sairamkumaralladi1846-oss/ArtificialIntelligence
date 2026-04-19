# Define the matrices A and B
A = [[1, 2], [3, 4]]  # Example: 2x2 matrix(mxn)
B = [[5, 6], [7, 8]]  # Example: 2x2 matrix(pxq)

# Get the dimensions of matrices A and B
m = len(A) 
n = len(A[0])
q = len(B[0])

# Initialize the result matrix C with zeros
C = [[0 for _ in range(q)] for _ in range(m)]

# Perform matrix multiplication using nested for loops
for i in range(m):
    for j in range(q):
        for k in range(n):
            C[i][j] += A[i][k] * B[k][j]

# Print the resulting matrix C
print("Resulting matrix C:")
for row in C:
    print(row)
