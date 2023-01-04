# Opens the file and reads the input data
with open("Day 1/input.txt", "r") as inputFile:
    inputData = inputFile.readlines()

# Converts the strings into ints
rationsPerElf = []
elf = []
for ration in inputData:
    ration = ration.removesuffix("\n")
    if ration == "":
        rationsPerElf.append(sum(elf))
        elf = []
    else:
        elf.append(int(ration))
rationsPerElf.sort()
rationsPerElf = rationsPerElf[::-1]

print(rationsPerElf[0], sum(rationsPerElf[0: 3]))