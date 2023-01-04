with open("Day 2/input.txt", "r") as inputFile:
    inputData = inputFile.readlines()

scores = []
# move = [first person, myMove, winner]
# 1: rock, 2: paper, 3: scissors
for move in inputData:
    move = move.removesuffix("\n")
    move = move.replace("X", "0")
    move = move.replace("Y", "3")
    move = move.replace("Z", "6")
    move = move.replace("A", "1")
    move = move.replace("B", "2")
    move = move.replace("C", "3")
    move = move.split(" ")
    moveToPlay = 0
    if move[1] == "3":
        moveToPlay = int(move[0])
    elif move[1] == "0":
        if move[0] == "1":
            moveToPlay = 3
        elif move[0] == "2":
            moveToPlay = 1
        elif move[0] == "3":
            moveToPlay = 2
    elif move[1] == "6":
        if move[0] == "1":
            moveToPlay = 2
        elif move[0] == "2":
            moveToPlay = 3
        elif move[0] == "3":
            moveToPlay = 1
    
    scores.append(int(move[1]) + moveToPlay)

print(sum(scores))