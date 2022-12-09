import tracemalloc

tracemalloc.start()
count = 0

fiboDict = {
            1 : 1 }

def fibonacci(num):
    global count
    count += 1
    if num in fiboDict.keys():
        return fiboDict[num]
    fiboDict[num] = num + fibonacci(num-1)
    return fiboDict[num]

for i in range(1, 100):
    fibonacci(i)
    
print(f"Count is {count}")

(memory, peak) = tracemalloc.get_traced_memory()

print(f"Memory usage is {memory / 10**3}KB; Peak was {peak / 10**3}KB")

tracemalloc.stop()
