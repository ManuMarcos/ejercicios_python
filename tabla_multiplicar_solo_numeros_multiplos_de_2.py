user_number=int(input("What number do you want a multiplication table:"))

for number in range(1,11):
    if number%2==0:
        result=user_number*number
        print("{} x {} = {}".format(user_number,number,result))
