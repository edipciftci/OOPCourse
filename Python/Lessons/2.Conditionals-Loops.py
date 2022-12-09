# Conditionals

if 1 < 2:
    print("Yes, 1 is less than 2")

###################################################################################################

number = input("Enter a number: ")

if int(number) < 0:
    print("The number is negative")
elif int(number) > 0:
    print("The number is positive")
else:
    print("The number is zero")

# ###################################################################################################

day = input("What day is it? ")

match day:
    case "Monday" | "monday" | "Tuesday" | "tuesday" | "Wednesday" | "wednesday" | "Thursday" | "thursday" | "Friday" | "friday":
        print("It's weekday")
    case "Saturday" | "saturday" | "Sunday" | "sunday":
        print("It's weekend")
    case _:
        print("That's not a day")

# Loops

for i in range(5):
    print(i)

print("New loop")

for i in range(2, 8):
    print(i)

print("New loop")  

# ###################################################################################################

num = 0
while num < 5:
    print(num)
    num += 1

print(num)
print("New loop")

# ###################################################################################################

for char in "Hello World":
    print(char)