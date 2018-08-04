user_string=input("Please enter a string:")

spaces=0
commas=0
points=0

for character in user_string:
    if character ==" ":
        spaces+=1
    elif character ==",":
        commas+=1
    elif character==".":
        points+=1

print("The amount of spaces in the string is:{}".format(spaces))
print("The amount of commas in the string is:{}".format(commas))
print("The amount of points in the string is:{}".format(points))



