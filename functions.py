#the sum of two numbers is define with return.

def adition (number_1, number_2):
    sum = number_1 + number_2
    return sum

number_1 = float(input('input the first number: '))
number_2 = float(input('input the second number: '))
print(adition(number_1, number_2))

#the sum of two number is define without return.

def adition():
    number_1 = float(input('input the first number: '))
    number_2 = float(input('input the second number: '))
    sum = number_1 + number_2
    print(sum)
    
adition()