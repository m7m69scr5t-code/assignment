import time
import matplotlib.pyplot as plt

def algo1(n):
    s = 0
    for i in range(n):
        s += i
    return s

def algo2(n):
    s = 0
    for i in range(n):
        for j in range(n):
            s += i + j
    return s

# Task 2: Increasing values of n
n_values = [100, 200, 400, 800, 1600]

times_algo1 = []
times_algo2 = []

# Task 3: Measure execution time for each run
for n in n_values:
    # Measure algo1
    start_time = time.perf_counter()
    algo1(n)
    end_time = time.perf_counter()
    times_algo1.append(end_time - start_time)
    
    # Measure algo2
    start_time = time.perf_counter()
    algo2(n)
    end_time = time.perf_counter()
    times_algo2.append(end_time - start_time)

# Task 4: Plot the graph
plt.figure(figsize=(10, 6))
plt.plot(n_values, times_algo1, label='algo1: O(n) (Linear)', marker='o', color='blue')
plt.plot(n_values, times_algo2, label='algo2: O(n²) (Quadratic)', marker='s', color='red')

plt.title('Algorithm Execution Time vs. Input Size (n)')
plt.xlabel('Input Size (n)')
plt.ylabel('Execution Time (seconds)')
plt.legend()
plt.grid(True)
plt.tight_layout()

# Show the plot
plt.show()