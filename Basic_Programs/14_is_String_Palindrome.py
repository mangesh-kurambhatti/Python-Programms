'''
	WAP to accept string & check if it is palindrome or not
'''

def isStringPalindrome(str1):
	
	y=str1[::-1]
	if(str1==y):
		print("palindrome")
	else:
		print("it is not palindrome")
	
	
	#for x in range(len(str1),0,-1):	
		#print(str(x))
	'''	
	if (str1==x):
		print("It is Palindrome..!")
		else:
		print("It is not Palindrome..!")
	'''	
def main():

	str1=eval(input("Enter the String:"))

	isStringPalindrome(str1)


if __name__=='__main__':
	main()
