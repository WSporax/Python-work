#Drawing a shape
# print("   /|")
# print("  / |")
# print(" /  |")
# print("/___|")

#Variables and datatypes
# character_name = "George"
# character_age = 35
# is_Male = True
# print("There once was a man named " + character_name + ",")
# print("he was ", character_age , " years old.")
# print("He really liked the name "+ character_name +",")
# print("but he didn't like being",character_age)

#Working with Strings
# phrase = "Giraffe Academy"
# print("Giraffe\n\"Academy\"")
# print(phrase + " is cool") #string concatanation. can use + since same data type
# print(phrase.lower()) # turns phrase into fully lower case
# print(phrase.upper()) # turns phrase into fully upper case
# print(phrase.isupper()) #returns false
# print(phrase.upper().isupper()) # isupper checks if string is uppercase, since upper is used, it will be
# print(len(phrase)) #number of characters in the string
# print(phrase[0]) #Gets the 1st character of phrase, here is G
# print(phrase.index("G")) #Should give back the index where G exists
# print(phrase.index("Academy")) #Should give index where Academy starts at 9th caharacter or [8] index
# #print(phrase.index("Z")) #Does not exist, should error, commenting out cause annoying
# print(phrase.replace("Giraffe", "Elephant")) #does what the method says

#Working with numbers
# print(2) #prints 2
# print(2.1)
# print(-2)
# print(3+4.5) #converts the answer into a float
# print(2*(3+4/2)) #BODMAS
# print(10%3) #gets remainder
# my_num = -5
# print(str(my_num)+ " is my favourite number") #needed to convert the number into a string for it to work concatanate with a string
# print(abs(my_num)) # converts the number into its absolute value -> -5 to 5
# print(pow(5, 2)) # 5^2
# print(pow(5, 16))
# print(max(1267,789876)) #which number is bigger
# print(min(142,167)) #which is smaller
# print(round(156.4)) #rounds down
# print(round(156.6)) #rounds up

# from math import * #importing the std python math functions
# print(ceil(156.5)) #goes up to 157
# print(floor(156.5)) #goes down to 156
# print(sqrt(25)) # does square root of 25

#Getting input
# name = input("Enter your name: ") # most simple get an input, insdie paranthesis is the display prompt. Stored in name variable
# age = input("Enter your age: ")
# print("Hello "+ name + " you are " + age) # prints out the info

#Basic Calculator
# num1 = input("Enter a number: ")
# num2 = input("Enter another number: ")
# result = int(num1) + int(num2) #python defaults inputs num1 and num2 into a string
# print(result) #this does not work with decimals, will error out, since expecting a string that can convert to an int
# num3 = input("Enter a number: ")
# num4 = input("Enter another number: ")
# betterResult = float(num1) + float(num2)
# print(betterResult) #this works on whole numbers and floats

# #madlibs game
# #basic structure
# print("Roses are red")
# print("Violets are blue")
# print("I love you")
# #madlibs structure
# color = input("Enter a colour: ")
# animal = input("Enter a group of animals: ") #etc schools of fish
# food = input("Enter your favourite food: ")
# print("Roses are " + color)
# print(animal + " are blue")
# print("I love "+food)

# #Lists
# friends = ["Keith", "Danny", "Richard", "Tim", "Sam"] # basic list structure, called friends, with 3 string values
# print(friends) # the whole list
# print(friends[0]) #prints the 0th index of friends, which is Keith
# print(friends[-1]) #prints out the last element of the list. -1 is the last element
# print(friends[1:3]) # prints out the 1st and 2nd indices or the 2nd and 3rd elements. [2,3] First parameter "1" is inclusive, 2nd parameter 3 is not
# print(friends[1]) # prints Danny
# friends[1] = "Joe" # replaces Danny with Joe
# print(friends[1]) # prints Joe as Danny has been replaced, rip Danny

#List Functions
# chill_numbers = [4,71,15,116,23,42]
# friends = ["Keith", "Danny", "Richard", "Tim", "Sam"] #taking the list from last exercise
# print(friends) #to check, print 
# friends.append("Tony") #Adds tony to the end of the list at the end
# friends.insert(2, "Houston") #Puts Houston in the 2nd index and pushes the rest 1 to the right
# friends.remove("Tim")
# print(friends) #Houston is now index 2, Tony is last element, Tim is gone
# print(friends.index("Danny")) #find Danny in the list and displays their position
# friends.pop() #removes last element "Tony" from the list
# print(friends) #Tony is gone
# friends.append("Keith") #adds another keith to end of list
# print(friends.count("Keith")) #Counts the number of Keiths in the list
# print(friends.sort) #sorts list in alphabetical order
# friends.clear() #clears the entire list
# print(friends) #now empty
# chill_numbers.sort()
# print(chill_numbers) #prints chill numbers list in ascending order
# #print(chill_numbers.sort()) #this errors??
# chill_numbers.reverse() #prints chill numbers list in descending order
# print(chill_numbers)
# friends = ["Keith", "Danny", "Richard", "Tim", "Sam"]
# friends2 = ["Jessie"]
# friends2 = friends
# print(friends2)

#Tuple
# coordinates = (14,15) #cannot change anythign about a tuple
# print(coordinates)
# print(coordinates[0]) #prints 14
#coordinates[1] = 10 #errors since can't change the value of index 1

#Functions
# def sayhi(): #basic af
#     print("Hello user")
# def say_hi(name, age):
#     print("Hello " + name + ", you are " + str(age)) #name parameter
# sayhi()
# say_hi("Nadim", 30)

# def cube(num):
#     return num*num*num
#     #code here does not execute, return breaks from function
# result = cube(4)
# print(result)

#if statements
# is_male = True
# is_tall = True

# if is_male and is_tall:
#     print("You are a tall male")
# elif is_male and not(is_tall):
#     print("You are a short male")
# elif is_male and not(is_tall):
#     print("You are not a male, but are tall")
# else:
#     print("You are neither male nor tall")

#if statements and comparisons
# def max_num(num1,num2, num3):
#     if num1 >= num2 and num1 >= num3:
#         return num1
#     elif num2 >= num1 and num2 >=num3:
#         return num2
#     else: 
#         return num3
# print(max_num(300,50,12)) #this covers all the possible variations of the three parameters

#Better calculator
# num1 = float(input("Enter the first number: "))
# op = input("Enter the operator: ")
# num2 = float(input("Enter the second number: "))

# if op == "+":
#     print(num1 + num2)
# elif op == "-":
#     print(num1 - num2)
# elif op == "/":
#     print(num1 / num2)
# elif op == "*":
#     print(num1 * num2)
# else:
#     print("Invalid operator")

#Dictionaries

# monthconversions = {
#     "Jan" : "January",
#     "Feb" : "February",
#     "Mar" : "March",
#     "Apr" : "April",
#     "May" : "May",
#     "Jun" : "February",
#     "Jul" : "February",
#     "Aug" : "February",
#     "Sep" : "February",
#     "Oct" : "October",
#     "Nov" : "November",
#     "Dec" : "December"
# }
# print(monthconversions["Jan"])
# print(monthconversions.get("Nov")) #both work the same
# print(monthconversions.get("dab", "Not a valid key")) # since dab is not a key, instead of printing none, will give the second parameter as an error message

#While loop
# i = 1
# while i<=10: #checks before looping
#     print(i) #prints 1,2,3....10
#     i += 1 #increments loop
# print("Done with loop")

#Guessing Game
# secret_word = "giraffe"
# guess = ""
# guess_count=0
# guess_limit = 3
# out_of_guesses = False

# while guess != secret_word and not out_of_guesses:
#     if guess_count < guess_limit:
#         guess = input("Enter your guess: ")
#         guess_count +=1
#     else: 
#         out_of_guesses = True

# if out_of_guesses == True:
#     print("You lose")
# else:
#     print("You lose")

#For Loops
# for letter in "Giraffe Academy": #letter was defined here
#     print(letter) #interpreted immediately as the chars in string
# friends = ["J-dawg", "J", "Jimothy"]
# for name in friends:
#     print(name)
# for index in range(len(friends)):
#     print(friends[index]) #everythign but the last number which would be the length of the array. for index of 0,1,2, the length is 3, so it goes up to 2
# for i in range (10):
#     print(i)
# for i in range (189,194):
#     print(i)
# for index in range(5):
#     if index == 0:
#         print("First iteration")
#     else:
#         print("Pass")

#exponent function
# print(2**3) # 2^3
# def raise_to_power(base_num, pow_num):
#     result = 1
#     for index in range(pow_num):
#         result = result*base_num
#     return result
# print(raise_to_power(3, 4))

#2d list and nesting
# number_grid = [
#     [1,2,3,4],[5],[6,7,8],[9,0]
# ]
# print(number_grid[0][1]) #first list index, then second index
# for row in number_grid:
#     print(row) #prints all top level elements which are lists
# for row in number_grid:
#     for nest_list in row:
#         print(nest_list) #for each top level list, print the inner elements of that list

#basic translator (TO FIX) (ELSE NOT EXECUTING)
# def translate(phrase): #change all vowels into g
#     translation = ""
#     for letter in phrase:
#         if letter in "AEIOUaeiou": #if letter variable is a char inside of the string 'AEIOUaeiou'
#             if letter.isupper():
#                 translation = translation + "g"
#             else:
#                 translation = translation + "g" #it would make it empty with translation, and then add G
#     else: 
#         translation = translation + letter #otherwise it would just assign the letter back to it
#     return translation
# print(translate(input("Please enter your string: ")))

#try/except
# number = int(input("Enter a number: ")) #throws an error 
# print(number)

try:
    number = int(input("Enter a number: "))
    value = 10/0 #this errors
    print(number)   
# except: #if anything errors with normal except, then its too broad, won't catch specific errors in the try block
#     print("Invalid Input")
except ZeroDivisionError:
    print("Divided by zero")
except ValueError:
    print("Invalid Input, not an int")
