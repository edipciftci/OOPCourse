def sumList(myList):
    sum = 0
    for i in myList:
        sum += i
    return sum

myList = [1, 2, 3, 4, 5]
print(sumList(myList))

###################################################################################################

def swap(name1, name2):
    temp = name1
    name1 = name2
    name2 = temp
    print("Name1: " + name1 + " Name2: " + name2)

name1 = "Edip"
name2 = "Elvin"

swap(name1, name2)

###################################################################################################

def factorial(n):
    fact = 1
    for i in range(n):
        fact *= (i + 1)
    return fact

print(factorial(5))