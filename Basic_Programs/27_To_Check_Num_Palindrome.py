#WAP to check no is palindrome or not


#def Reverse(num1):
#	reverse=0
	
def IsPalindrome(num1):
	number=num1	
	reverse=0
	rem=0
	while num1>0:
		rem=num1%10
		reverse=reverse*10+rem
		num1=num1//10
	if number==reverse:
		return 1
		#print("No is Palindrome")
	else:
		return 0
		#print("No is NOT palindrome")


def main():
	
	num1=eval(input("Enter the no: "))

	if IsPalindrome(num1):
		print("Palindrome")
	else:
		print("Not Palindrome")

if __name__=='__main__':
	main()
