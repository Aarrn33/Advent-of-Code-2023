# Read data
with open("Day 3/input.txt", "r") as inputFile:
    inputData = inputFile.readlines()

# Formats data
inputData = [line.removesuffix("\n") for line in inputData]

# Separates the two equal halves
backpackHalves = []
for backpack in inputData:
    halfpoint = len(backpack)//2
    firstHalf = backpack[0:halfpoint]
    secondHalf = backpack[halfpoint:]
    backpackHalves.append([firstHalf, secondHalf])

# Finds the common letter
commonLetters = []
for backpack in backpackHalves:
    letterInCommon = ''.join(set(backpack[0]).intersection(backpack[1]))
    commonLetters.append(letterInCommon)

# Converts the letters to corresponding priorities
letterPriorities = []
for letter in commonLetters:
    if letter == letter.lower():
        priority = ord(letter)-96
    else:
        priority = ord(letter)-38
    letterPriorities.append(priority)

print(sum(letterPriorities))
