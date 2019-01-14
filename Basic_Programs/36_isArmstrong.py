def isArmstrong(num):
	remiander=0;
	sum1=0
	num1=num

	while num>0:
		remainder=num%10
		sum1=sum1+(remainder*remainder*remainder)
		num=num//10

	if num1==sum1:
		return True
		#print("Success")
	else:
		return False
		#print("fail")
def main():
	
	num=eval(input("Enter the number :"))

	if isArmstrong(num):
		print("{} is armstrong number".format(num))
	else:
		print("{} is not Armstrong number".format(num))

if __name__=='__main__':
	main()
