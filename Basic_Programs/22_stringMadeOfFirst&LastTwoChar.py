'''

	 Write a program to accept a string from user and display a string made of 1st two & last two character. Alternate characters.
	Hint: display alternate character starting with 1. Jeetendra=Jera
'''
def ConcatinateFirtsAndLastTwoChar(str1):
	y=str1[:2:]
	z=str1[-2::]

	print("After combining 1st two and last two character string is:",y+z)
	

def main():
	str1=eval(input("Enter the string:"))

	ConcatinateFirtsAndLastTwoChar(str1)

if __name__=='__main__':
	main()

'''
	********output************
	
mangesh@mangesh-VPCEH35EN:~/10th Python Batch/Basic Programs$ python3 22_stringMadeOfFirst\&LastTwoChar.py 
Enter the string:"Jeetendra"
After combining 1st two and last two character string is: Jera

'''
