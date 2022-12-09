# Basic print commands

print("Hello World")
print("Hello" + "World")
print("Hello", "World")
print("Hello", "World", sep="***", end="!!!")
print("\n")

print(2 + 5)
print(2 - 5)
print(2 * 5)
print(2 ** 5)

print(2 / 5)
print(2 // 5)
print(9 // 5)

print(2 % 5)
print(9 % 5)

print(2 > 5)
print(2 < 5)
print(2 == 5)
print(2 != 5)

###################################################################################################

# Variables

first_name = "John"
middle_name_initial = "T"
last_name = "Doe"
age = 25
height = 1.75
is_blonde = True

print("First Name:", first_name)
print("Last Name: " + last_name)
print("Age: " + str(age))
print("Height: {}".format(height))
print("Is {} a blonde? {}".format(first_name, is_blonde))
print("{0} {1}. {2} is {3} years old and {4} meters tall. {0} is a human.".format(first_name, middle_name_initial, last_name, age, height))

###################################################################################################

# Input-Output (I/O)

name = input("What is your name? ")
print("Hello, " + name + "!")

answer = input("What is 3 + 5? ")
print("You answered: " + answer)
result = int(answer) == 8
print("{}, your answer is {}.".format(name, result))

print("Name of the user is: {}".format(input()))
