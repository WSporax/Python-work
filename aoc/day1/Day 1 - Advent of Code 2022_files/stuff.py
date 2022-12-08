arr1 = []
arr2 = [1,2,3,4]

i = 0
while(i<len(arr2)):
    arr1.append(0)
    arr1[i] += arr2[i]
    i+=1
print(arr1)