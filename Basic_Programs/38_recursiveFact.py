def RecursiveFactorial(num1):

	
	if num1==0:
		return 1;
	return num1*RecursiveFactorial(num1-1)
		
	

def main():
	num1=eval(input("Enter the number:"))
	
	result=RecursiveFactorial(num1)

	print("Resulty is:",result)
if __name__=='__main__':
	main()
