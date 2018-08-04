user_string=input("Please enter  a string:")
list_mayus_letters=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
mayus_letters=0
for character in user_string:
    if character in list_mayus_letters:
        mayus_letters+=1
print("The amount of mayus letters is {}".format(mayus_letters))



