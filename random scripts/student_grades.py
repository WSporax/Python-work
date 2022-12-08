# Define a list of tuples that contain information about a student grades. Each tuple in the list 
# is containing the following information (subject name, mark and credits number)
# Calculate the mean of the student grads (m1 + m2 + mn)/n where mi represents the mark of the
# student at subject i and n is the number of marks
# Calculate the weighted mean of the student grades (m1w2 + m2w2+...+mnwn)/(w1+w2+...+wn)
# where wi represents the number of credits allocated to subject i.

# student_name= ('Joe','Lee', 'xie-ut','Esteban', 'Julio', 'Ricardo','Montoya', 'Delarossa', 'Ramirez')
# student_mark = (60,67,65,88,75,77,23,55,98,)
# student_credit = (30, 30, 35, 10, 40, 40, 10, 30, 20)

# student_info = [student_name, student_mark, student_credit]

# def calcul_medie(mark_list):
#     cumul_grad = 0
#     for i in mark_list:
#         cumul_grad= cumul_grad+i
#     n = cumul_grad/(len(mark_list))
#     return n
# def weighted_mean(mark_list, credit_list):
#     cumul_weight_grad = 0
#     cumul_credit = 0
#     for i in credit_list:
#         cumul_credit = cumul_credit +i
#     for j in range(1, len(mark_list), 1):
#         cumul_weight_grad= mark_list[j] * credit_list[j]
#     wn = cumul_weight_grad/cumul_credit
#     return wn, cumul_credit, cumul_weight_grad
# print(calcul_medie(student_info[1]))
# print(weighted_mean(student_info[1], student_info[2])) #outputs 8.0, seems way too low

#Write a program that creates a dictionary that contains for each person its name and phone number
#Display dict content. #Display dict content in alphabetical order of person names
book_dict = {}
def phonebook(p_name,p_phone):
    book_dict[p_name] = int(p_phone)
    return book_dict

def order_dict(unordered_book_dict):
    key_olist = [] #list which contains the keys in the unorderd dict
    ordered_book_dict = {} #function dict for the ordered key pair values
    for order in unordered_book_dict: # iterate all keys in the unorderd dict
        key_olist.append(order) # add the keys to the dict_key_order list
    key_olist.sort() #sort the list into alphabetical order
    for i in range(len(key_olist)): #iterate through the alphabetical key list
        ordered_book_dict[key_olist[i]] = unordered_book_dict.get(key_olist[i])
    unordered_book_dict = ordered_book_dict
    return unordered_book_dict

user_add = input("Would you like to add a name to the phonebook? Please indicate y/n: ")

if user_add == 'y':
    n_contact = int(input("Indicate the number of people you would like to add: "))
elif user_add == 'n':
    print("Exiting phonebook")
else:
    print("Invalid statment, please restart the application")

for contacts in range (n_contact):
    if user_add == 'y':
        new_name = input("Please enter the name of the new contact: ")
        new_num = input("Please enter the phone number of the new contact: ")
        phonebook(new_name, new_num)
        print(new_name + ": " + str(new_num) + " has been added to the phonebook")
    elif user_add == 'n':
        print("Exiting phonebook")
    else:
        print("Invalid statment, please restart the application")
#print("Current contacts in the phonebook: " + str(book_dict))
print(order_dict(book_dict))
print(book_dict)