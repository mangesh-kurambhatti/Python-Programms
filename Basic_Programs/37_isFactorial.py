def Factorial(num1):

	fact=1;
	if num1>1:
		for x in range(1,num1+1):
			fact=fact*x
		return fact
	else:
		return False
		
def FactorialBySir(num1):

	fact=-1
	if num1>0:
		if num1<3:
			fact=num1
		else:
			fact=1
			while(num1 != 1):
				fact=fact*num1
				num1-=1
				
	return fact
			
def main():
	num1=eval(input("Enter the no:"))

	result=Factorial(num1)

	print("Factorial of {} is:{}".format(num1,result))
	

	result1=FactorialBySir(num1)

	print("Factorial of {} by sir is:{}".format(num1,result1))
	
if __name__=='__main__':
	main()
