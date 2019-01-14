# WAP to MENUDRIVEN of Arithmatic Operation
import sys

def Addition(num1,num2):
	return num1+num2
def Substraction(num1,num2):
	return num1-num2

def Multiplication(num1,num2):
	return num1*num2

def Division(num1,num2):
	return num1/num2

def main():

	while True:
		print("1.Addition")
		print("2.Substraction")
		print("3.Multiplication")
		print("4.Division")
		print("5.Exit")

		ch=eval(input("Enter your choice :"))

		num1=eval(input("Enter your 1st no:"))

		num2=eval(input("Enter your 2nd no:"))	
	

	
		if ch==1:
			print("Addition of {} and {} is {}".format(num1,num2,Addition(num1,num2)))
		elif ch==2:
			print("Substraction of {} and {} is {}".format(num1,num2,Substraction(num1,num2)))
		elif ch==3:
			print("Multiplication of {} and {} is {}".format(num1,num2,Multiplication(num1,num2)))
		elif ch==4:
			print("Division of {} and {} is {}".format(num1,num2,Division(num1,num2)))
		elif ch==5:
			sys.exit
		else:
			print("Invalid choice")	

if __name__=='__main__':
	main()
