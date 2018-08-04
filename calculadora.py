"""Calculadora que le pregunta al usuario que operacion quiere hacer, a la vez
que dos numeros con los que operara"""

operation=input("What operation do you want to do? (multiplication/division/sum/substraction):").upper()
number1=int(input("First number:"))
number2=int(input("Second number:"))
if operation=="MULTIPLICATION":
    result=number1*number2
elif operation=="DIVISION":
    result=number1/number2
elif operation=="SUM":
    result=number1+number2
else:
    result=number1-number2
print("The result of this operation is {}".format(result))

