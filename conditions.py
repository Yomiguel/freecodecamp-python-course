#----------------------------------------if statements----------------------------------------

def comparation_numbers(number_1, number_2):
    if number_1 == number_2:
        print(str(number_1) + ' is equal to ' + str(number_2))
    elif number_1 > number_2:
        print(str(number_1) + ' is greater to ' + str(number_2))
    else:
        print(str(number_1) + ' is less than ' + str(number_2))

number_1 = float(input('please enter the fisrt number: '))
number_2 = float(input('please enter the second number: '))
comparation_numbers(number_1, number_2)

#--------------------------------------------**************---------------------------------------------#