#//WAP to find the GCD of two no
def isGCD(num1,num2):
	
	while(num1!=num2):
		if(num1<num2):
			num2=num2-num1
		elif num1>num2:
			num1=num1-num2
	return num1
def main():
	num1,num2=eval(input("Enter the num1 and num2 :"))
	
	result=isGCD(num1,num2)
	print("GCD is:",result)
if __name__=='__main__':
	main()
