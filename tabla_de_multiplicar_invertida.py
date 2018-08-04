user_number=int(input("What number do you want a multiplication table:"))
counter=10
while counter!=0:
    result=user_number*counter
    print("{} x {} = {}".format(user_number,counter,result))
    counter-=1

