user_number=int(input("What number do you want a multplication table:"))

for number in range(5,16):
    result=user_number*number
    print("{} x {} = {}".format(user_number,number,result))
