#*************-----------------------this program replaces words in a phrase requested by the user----------------------***********

pharse = input('please, input your phrase ')
print('your sentence is : ' + pharse)
word1 = input('please, input the word you wish to replace')
word2 = input('please type the word you wish to input')
print(pharse.replace(word1, word2))