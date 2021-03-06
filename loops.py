#----------------------------------------loops in python----------------------------------------#

#----------------------------------------while----------------------------------------#

#this part of the code prints the numbers from one to ten.
i = 1
while i <= 10:
    print(i)
    i +=1

#----------------------------------------for----------------------------------------#

#this part of the code prints the numbers from one to ten.
for i in range (10):
    print(i+1)

#this part of the code prints the letters in of a word.
for i in 'luis':
    print(i)

#this part of the code prints the values in a list.
names = ['luis', 'miguel']
for i in names:
    print(i) 

#this part of the code prints the values in a list and stops at the indicated value.
names = ['luis', 'miguel', 'jimenez', 'castro']
for i in names:
    print(i)
    if i == 'jimenez':
        break 

#----------------------------------------nested loops----------------------------------------#

#this part of the code declares a matrix
x = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h','i']
]

#this part of the code prints all elements of the matrix
for i in x:
    for y in i:
        print(y) 

#this part of the code prints the type of the variable stored in the list.
elements3 = ['luis', 10, 'jimenez', False] 
for i in elements3:
    print(type(elements3[elements3.index(i)]))