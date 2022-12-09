numbers = [1, 3, 4, 5, 6, 9, 11, 23]
sum = 9
# sum = 18
ansFound = False

for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        if numbers[i] + numbers[j] == sum:
            print(str(numbers[i]) + " and " + str(numbers[j]))
            ansFound = True

if not ansFound:
    print("No answer")
