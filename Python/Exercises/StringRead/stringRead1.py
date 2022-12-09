text = "this is an example string to be read by the code"

letterCount = [['a', 'b', 'c', 'd'], [0, 0, 0, 0]]

for char in text:
    for i in range(len(letterCount[0])):
        if char == letterCount[0][i]:
            letterCount[1][i] += 1

print(letterCount)