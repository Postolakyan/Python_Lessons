#Exercise 1; 
# Given a string of odd length 7, return a new string made of the middle three characters of 
# a given String


def stringConvert(word):
	'''This function prints the three 
	letters in the middle of the entered word'''
	x=int(len(word)/2)
	res=(word[x-1:x+2])
	print("The result = "+res)
	print(stringConvert.__doc__) 

word=input("Please enter an odd word longer than 7  ")
if len(word)>7 and len(word)%2!=0 and type(word)==type("string"):
    stringConvert(word)
else:
    print("The word does not match the given terms  ")


#Exercise 2;
# Given two strings s1 and s2, create a new string by appending s2 in the middle of s1


def String(word1,word2):
	'''This function places the second word in the 
	middle of the first word and prints it on the screen'''
	mid=word1[:len(word1)//2]
	mid2=word1[len(word1)//2:]
	result=mid+word2+mid2
	print("The result = ",result)
	print(String.__doc__)
    

string1= input("Please insert the first string   ")
string2= input("Please insert the second string   ")
String(string1,string2)
