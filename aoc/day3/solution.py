def split_compartments(line: str) -> list[set]:

    return[set(line[:len(line) //2 ]), set(line[len(line)//2:]) ]


fileDay3 = open(r"D:\From C Drive\Code\Python\aoc\day3\input.txt", "r")
for line in fileDay3:
    print(line)
    print(split_compartments(line))