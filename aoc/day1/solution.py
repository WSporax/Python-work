fileDay1 = open(r"day1\input.txt", "r")
lines = fileDay1.readlines()

print(f"length of lines is {len(lines)}")
lines =' '.join(lines).split("\n\n")
lines = '\n'.join(lines).split("\n")
print(''.join(lines).split(" "))

str_input = '\n'.join(lines)

summed_arr = []
num_of_elves = 0
i=0
while(i<len(lines)):
    try:
        type(int(lines[i-1])) == int      
        print(lines[i])
        summed_arr.append(0)
        summed_arr[num_of_elves] += lines[i]
        i+=1

    except:        
        num_of_elves+=1        
        i+=1

print(summed_arr)
print(num_of_elves)
