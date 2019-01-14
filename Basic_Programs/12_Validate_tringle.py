#!/usr/bin/python

def isValidTraingle(num1,num2,num3):
	if((num1+num2)>num3):
		print("It can form a Tringle..!")
	else:
		print("It can't form a Triangle..!")
def main():
	
	num1=eval(input("Enter the 1st number :"))
	num2=eval(input("Enter the 2nd number :"))
	num3=eval(input("Enter the 3rd number :"))

	isValidTraingle(num1,num2,num3)


if __name__=='__main__':
	main()
