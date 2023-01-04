# Reads the input file
with open("Day 4/input.txt", "r") as inputFile:
    inputData = inputFile.readlines()

# Cleans the data
inputData = [line.removesuffix("\n") for line in inputData]
