import time
import threading
import multiprocessing

numbers = [2, 3, 4, 5]
results = []  # Global variable (threads will share this, processes won’t)

# Function to calculate square
def calc_square(nums):
    global results
    for n in nums:
        time.sleep(1)  # Simulate heavy task
        results.append((n, "square", n * n))
        print(f"[{threading.current_thread().name}] Square of {n}: {n*n}")

# Function to calculate cube
def calc_cube(nums):
    global results
    for n in nums:
        time.sleep(1)
        results.append((n, "cube", n * n * n))
        print(f"[{threading.current_thread().name}] Cube of {n}: {n*n*n}")


### 🔹 1. Sequential Execution
start = time.time()
calc_square(numbers)
calc_cube(numbers)
print("\nSequential results:", results)
print("Time taken (sequential):", time.time() - start, "\n")


### 🔹 2. Multithreading
results = []  # Reset
start = time.time()
t1 = threading.Thread(target=calc_square, args=(numbers,), name="Thread-Square")
t2 = threading.Thread(target=calc_cube, args=(numbers,), name="Thread-Cube")

t1.start()
t2.start()
t1.join()
t2.join()

print("\nThreading results (shared global list):", results)
print("Time taken (threading):", time.time() - start, "\n")


### 🔹 3. Multiprocessing
# Reset is irrelevant because processes won't share the global list
results = []  # Reset
start = time.time()
p1 = multiprocessing.Process(target=calc_square, args=(numbers,))
p2 = multiprocessing.Process(target=calc_cube, args=(numbers,))

p1.start()
p2.start()
p1.join()
p2.join()

print("\nMultiprocessing results (no shared global list):", results)
print("Time taken (multiprocessing):", time.time() - start, "\n")
