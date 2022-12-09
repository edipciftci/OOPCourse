# Lists

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

today = input("What day is it? ")

dayNum = days.index(today)

print("In 13 days it will be " + days[(dayNum + 13) % 7])

###################################################################################################

myList = []

for i in range(7):
    myList.append(i)

print(myList)

for num in myList:
    print(num)

list2 = [7, 8, 3, 2, 1, 9, 0, 4, 5, 6]

myList.remove(3)
print(myList)

myList[4] = -3
print(myList)

myList.pop(4)
print(myList)

myList.pop()
print(myList)

myList.sort()
print(myList)

myList.reverse()
print(myList)

myList.extend(list2)
print(myList)

myList.sort()
print(myList)

###################################################################################################

food = [["Apple", "Banana", "Orange"], ["Pizza", "Burger", "Hotdog"], ["Carrot", "Broccoli", "Celery"]]
foodTypes = ["Fruit", "Fast Food", "Vegetable"]

print(food)
print(food[0])
print(food[0][1])

print("\n")

food[1].append("Fries")
print(food)

food.append(["Pasta", "Rice", "Bread"])
foodTypes.append("Grain")
for type in foodTypes:
    print("\n")
    line = type + ": "
    for item in food[foodTypes.index(type)]:
        line += item + " "
    print(line)

###################################################################################################

# Strings

myName = "edip Çiftçi"
print(myName[0])

myName = myName.capitalize()
print(myName)

myName = "Edip Çiftçi"

print(myName.replace("Edip Çiftçi", "Elvin Denk"))
print(myName)

newName = myName.replace("Edip Çiftçi", "Elvin Denk")
print(newName)

print(myName.find("Çiftçi"))
print(myName.find("Denk"))

print(myName.index("i"))
print(myName.count("i"))

print(myName[0:8])
