user_string=input("Enter a string:")
vowels_in_string=[]
for character in user_string:
    vowels="aeiou"
    if character in vowels:
        vowels_in_string.append(character)
print("The vowels in the string are:{}".format(vowels_in_string))

