with open("Day 2/input.txt", "r") as inputFile:
    inputData = inputFile.readlines()

scores = []
# move = [first person, myMove, winner]
# 1: rock, 2: paper, 3: scissors
for move in inputData:
    move = move.removesuffix("\n")
    move = move.replace("X", "1")
    move = move.replace("Y", "2")
    move = move.replace("Z", "3")
    move = move.replace("A", "1")
    move = move.replace("B", "2")
    move = move.replace("C", "3")
    move = move.split(" ")
    score = 0
    if move[0] == move[1]:
        score = 3
    elif move[0] == "1":
        if move[1] == "2":
            score = 6
        elif move[1] == "3":
            score = 0
    elif move[0] == "2":
        if move[1] == "1":
            score = 0
        elif move[1] == "3":
            score = 6
    elif move[0] == "3":
        if move[1] == "1":
            score = 6
        elif move[1] == "2":
            score = 0
            
        scores.append(score + int(move[1]))

print(sum(scores))