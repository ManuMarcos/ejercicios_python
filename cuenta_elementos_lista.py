user_number_list = []
counter = 0
fin = False
while not fin:
    try:
        user_number = int(input("Please enter a number:"))
        user_number_list.append(user_number)
        counter += 1
    except ValueError:
        print("List= {}".format(user_number_list))
        print("List long= {}".format(counter))
        break

