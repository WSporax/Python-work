"""
l = [3, 6, 9]
print(l)

l = ['ana', 'has', 'appels']
print(l)

l = ['Maria', 20, 'Ion', 30.6]
print(l)

l = ['ana', 'has', 'appels']
print(l)
print('first element:', l[0])
print('second element:', l[1])
print('third element:', l[2])

L= ["ana", "has", "appels"]
print("List has" , len(L), "elements")

L= ['a', 'b', 'c', 'd']
print(l[1])

l = []
print('empty list', l)

print(list(range(0, 10, 2)))
print(list(range(0, 10,)))
L= [i**3 for i in range(5)]
print(L)
"""
""" oscar pls hlp
G= [1, 2, 3, 4, 5, 6, 7, 8]
print(G)
for i in range(3):
    del G[i]
print(G)
"""
"""
L = [4,5,-2,6]
L.reverse()
print('reversed list', L)
L.sort()
print('sorted list', L)
"""
"""Ghost is switching out the outputs
S = set()
S.add("red")
print(S)
S.add("orange")
print(S)
S.add("red")
print(S)
S.remove("red")
print(S)
S.add("red")
print(S)
S.add("red")
print(S)
S.add("red")
print(S)
S.add("green")
print(S)
S.remove("green")
print(S)
S.add("green")
print(S)
"""
"""
#Ex 1 Display the first N natural numbers

i = int(input())

inputList = list(range(i))
print(inputList)
"""
"""
#Ex 2 Define a list of user names and write a program that search if a username appears in a list
userList = []

for i in range(6):
    print('username no: '+ str(i+1))
    userList.insert(i, str(input()))

print('Which name do you want to search for?')
if str(input()) in userList:
    print("Yes it exists")
else:
    print("nah your princess is another castle")
"""
"""
def changeme( mylist ):
   "This changes a passed list into this function"
   mylist.append([1,2,3,4])
   print("Values inside the function:", mylist)
   return

mylist = [10,20,30]
changeme(mylist)
print('values outside the function', mylist)
"""
#Exercise 3

schoolRecord = []
print("Please pick a number\n1. Add a student \n2. Calculate the average mark \n3. Calculate the average number of credits \n4. View School record")

def studentInfo():
    print('Write the name, the mark and the number of credits for each student')
    t = (str(input()), float(input()), int(input()))
    schoolRecord.append(t)
    
#def averageMark():
    #for i in schoolRecord

#def averageCreditScore():

n = int(input())-1

options = {0 : studentInfo(), 1 : averageMark(), 2: averageCreditScore(), 3: print(schoolRecord)}
#studentInfo()
#print(schoolRecord)