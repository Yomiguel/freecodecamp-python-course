#----------------------------list in python---------------------------#

#this part of code declares a list.
elements = ['luis', 15, False, 21.3]
print(elements)

#this part of code declares a list.
elements1 = list(('luis', 15, False, 21.3))
print(elements1)

#this part of the code prints the type of the variable stored in the list.
print(type(elements[0]), type(elements[1]), type(elements[2]), type(elements[3]))

#this part of the code prints the variable stored in the indicated position, in this case third one.
print(elements[3])


#----------------------------list Methods---------------------------#

#this part of code declares a two lists and prints their contents.
elements3 = ['luis', 'miguel', 'jimenez', 'castro']
elements4 = [10, 20, 30, 40]
print(elements3, elements4)

#this part of the code adds the items in the list 'elements4' to the end of the list 'elements3'
elements3.extend(elements4)
print(elements3)

#this part of the code adds a new element the specified value to the end of the list.
elements4.append(50) 
print(elements4)

#this part of the code shows the number of elements in list.
print(len(elements4))

#this part of the code insert the element specified in the position indicated.
elements4.insert(2, 100)
print(elements4)

#this part of the code sort the elements in the list.
elements4.sort()
print(elements4)

#this part of the code clear the elements in the list.
elements4.clear()
print(elements4)

#----------------------------Tuples in python---------------------------#

#this line declares a tuple.
tupla1 = (1, 2, 3, 4, 5, 4, 3, 2, 1)
tupla2 = tuple((1, 3, 2, 3, 1))
print(tupla1, tupla2)