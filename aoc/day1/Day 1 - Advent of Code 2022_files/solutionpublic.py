fileday1 = open(r"day1\input.txt", "r")
intermediate_arr = []
summed_arr = []
for line in fileday1:
  try:
    intermediate_arr.append(int(line))
  except:
    summed_arr.append(sum(intermediate_arr))
    intermediate_arr.clear()
summed_arr.append(sum(intermediate_arr))
print(summed_arr)
print(f"Elf {summed_arr.index(max(summed_arr))} has the largest calories of {max(summed_arr)},and says there are {sum(summed_arr)} calories in total.")
