"""Le pregunta a un usuario el numero a adivinar , luego le
pregunta a otro usuario cual es el numero ingresado"""

number_to_guess=input("Please enter one number to guess:")
inputted_number=input("Enter one number:")
while inputted_number!=number_to_guess:
    print("The number you entered is not the number to guess")
    inputted_number = input("Input one number:")
print("The number you entered is the number to guess and it is {} , Congratulations!!!".format(number_to_guess))

