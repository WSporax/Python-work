#list all possible permutations of rps hands
dictDay2P1 = {
    "A X" : 4,
    "A Y" : 8,
    "A Z" : 3,
    
    "B X" : 1,
    "B Y" : 5,
    "B Z" : 9,
    
    "C X" : 7,
    "C Y" : 2,
    "C Z" : 6,
}

dictDay2P2 = { #rock: A paper: B Scissors = C. Draw = Y (same), lose = X, win = Z.
    "A X" : 3, #Rock Scissors
    "A Y" : 4, #Rock Rock
    "A Z" : 8, #Rock Paper
    
    "B X" : 1,
    "B Y" : 5,
    "B Z" : 9,
    
    "C X" : 2,
    "C Y" : 6,
    "C Z" : 7,
}

fileDay2 = open(r"D:\From C Drive\Code\Python\aoc\day2\input.txt", "r")

pointsCount = 0


for line in fileDay2:
  pointsCount += dictDay2P1[line.split("\n")[0]]

print(pointsCount)

#solution day 2
#need to open the file again for some reason?
fileDay2P2 = open(r"D:\From C Drive\Code\Python\aoc\day2\input.txt", "r")

sum1 = 0
for line in fileDay2P2:
  sum1 += dictDay2P2[line.split("\n")[0]]


print(sum1)