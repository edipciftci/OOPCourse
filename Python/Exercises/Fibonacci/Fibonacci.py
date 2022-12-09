import tracemalloc

tracemalloc.start()
count = 0

def fibonacci(num):
    global count
    count += 1
    if num == 1:
        return 1
    return num + fibonacci(num-1)

for i in range(1, 100):
    fibonacci(i)

print(f"Count is {count}")

(memory, peak) = tracemalloc.get_traced_memory()

print(f"Memory usage is {memory / 10**3}KB; Peak was {peak / 10**3}KB")

tracemalloc.stop()