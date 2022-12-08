# l = [9, -4, 15, 8 , -30, 8]
# ldivisible= []

# for i in l:
#     if i%5 ==0:
#         ldivisible.append(i)
#         continue
# print(ldivisible)

# u got a dictionary with numbers, no matter what the name of the key is.
# print all the numbers from that dictionary which are divisible with 5, together with the name of the key they belong to.
# ex: dict={'Ages' : [1,2,3,4,5,6,7,8,9,10] , 'Father_Ages': [50, 100, 13], 'Mother_ages': [15, 16, 17]}
# output will be: 5 'Ages' ,10 'Ages', 50 'Father_Ages' ...
#for dictionaries, finding the values can be understood by saying dict[key] = value
#so for key in dict, key = all the keys iterated
#and the values are therefore

#Example idk what happened here
# divisor = 7
# divisible_criteria = False
# j_dict ={'Ages' : [1,2,3,4,5,6,7,8,9,10], 'Father_Ages': [50, 100, 13], 'Mother_ages': [15, 16, 17]}
# # for key in j_dict:
# #     print(key, ' ', j_dict[key])

# for key in j_dict:
#     divisible_criteria = False
#     for elem_of_val in j_dict[key]: #j_dict[key] = all the values of the dict
#         if elem_of_val % divisor ==0:
#             print(elem_of_val, ' is divisible by '+ str(divisor) + ', present in ', key)
#             divisible_criteria = True

#         # else: #Don't like a print statement for every value that is not divisible
#         #     print("No values in the key "+ str(key) +" are divisible by " + str(divisor))
#     if divisible_criteria == False:
#         print('There are no elements divisible by ' + str(divisor) + 'inside of the key ' + str(key))
