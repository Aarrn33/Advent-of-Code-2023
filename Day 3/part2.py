# Read data
with open("Day 3/input.txt", "r") as inputFile:
    inputData = inputFile.readlines()

# Formats data
inputData = [line.removesuffix("\n") for line in inputData]

# Separates the groups of three
backpackGroups = []
beginningRank = 0
for i in range(len(inputData)//3):
    group = inputData[beginningRank:beginningRank+3]
    backpackGroups.append(group)
    beginningRank += 3

# Gets the common letters of each group
commonLetterPerGroup = []
for group in backpackGroups:
    letterInCommon = ''.join(set(group[0]).intersection(group[1]).intersection(group[2]))
    commonLetterPerGroup.append(letterInCommon)

# Converts the letters to corresponding priorities
letterPriorities = []
for letter in commonLetterPerGroup:
    if letter == letter.lower():
        priority = ord(letter)-96
    else:
        priority = ord(letter)-38
    letterPriorities.append(priority)
print(sum(letterPriorities))
