#-------------------------reading files--------------------------

# 'r' for reading only, 'w' for writing only, 'r+' for writing and reading, 'a' for append.
file_names = open("names.txt","a")

""" #this line print the state of the file (r(readable), w(wirtable), r+ or a).
print(file_names.writable()) 

#this line print the first line of the file.
print(file_names.readline()) 

#this line print the lines of the file as a list.
print(file_names.readlines()) 

#this part of the code print line by line the file.
for i in file_names.readlines():
    print(i) 

#this line print the third line in file.
print(file_names.readlines()[2]) """

#-------------------------writing files--------------------------

#this line adds the element 'peru' to the final line of the file.
file_names.write('\nPeru')

# 'r' for reading only, 'w' for writing only, 'r+' for writing and reading, 'a' for append.
file_names = open("names.txt","r")

#this part of the code print line by line the file.
for i in file_names.readlines():
    print(i) 

#this line close the file.
file_names.close