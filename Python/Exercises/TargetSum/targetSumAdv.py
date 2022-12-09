numbers = [1, 3, 4, 5, 6, 9, 11, 23]
sum = 9
# sum = 18
ansFound = False

leftNum = numbers[0]
rightNum = numbers[-1]

while leftNum != rightNum:
    currSum = leftNum + rightNum
    if currSum == sum:
        ansFound = True
        print(str(leftNum) + " and " + str(rightNum))
        leftNum = numbers[numbers.index(leftNum) + 1]
        continue
    if currSum < sum:
        leftNum = numbers[numbers.index(leftNum) + 1]
        continue
    if currSum > sum:
        rightNum = numbers[numbers.index(rightNum) - 1]

if not ansFound:
    print("No answer")
