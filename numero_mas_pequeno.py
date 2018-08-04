user_number_list=[]
user_number=input("Please enter a number:")
min_number=999999
while len(user_number_list)<10:
    while not user_number.isdigit():
        user_number = input("The character you entered is not a number, please enter a number:")
    user_number_list.append(user_number)
    if int(user_number)<min_number:
        min_number=user_number
    user_number=input("Please enter a number:")
print(min_number)
print(user_number_list)





