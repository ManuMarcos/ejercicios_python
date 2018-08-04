accumulator=0
counter=0
user_number_list=[]
fin=False
while not fin:
    try:
        user_number=int(input("Please enter a number:"))
        user_number_list.append(user_number)
        accumulator+=user_number
        counter+=1
    except:
        average=accumulator/counter
        print("List: {}".format(user_number_list))
        print("The average is: {}".format(average))
        break
