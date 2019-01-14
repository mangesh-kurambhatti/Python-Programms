# Recursion for GCD number
def isGCD(no1,no2):
	if no1==no2:
		return no1
	elif no1>no2:
		return isGCD(no1-no2,no2)
	else:
		return isGCD(no1,no2-no1)		


def main():
	no1,no2=eval(input("Enter the number1 and number2 :"))
	result=isGCD(no1,no2)
	print("GCD of {} and {} is :{}".format(no1,no2,result))
if __name__=='__main__':
	main()
