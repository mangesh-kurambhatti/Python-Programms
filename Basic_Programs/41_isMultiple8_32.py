def isMultipleOfEightBySir(num1):
	if num1&7==0:
		print("Multiple of 8 by sirs Logic")
	else:
		print("Not multiple")

def isMultipleOf32(num1):
	if num1&31==0:
		print("Multiple of 32");
	else:
		print("not Multiple of 32");
'''

def isMultipleOfEightByMe(num1):
	if num1>8:
		if num1 & (num1+1)==0:
			print("Multiple of 8 by my logic")
		else:
			print("not multiple")  
	else:
		print("Enter the no greater than 8")
'''
def main():
	
	num1=eval(input("Enter the number :"))
	
	print("1.Multiple of 8")
	print("2.Multiple of 32")
	
	ch=eval(input("Enter your choice :"))
	
	#isMultipleOfEightByMe(num1)
	if ch==1:
		isMultipleOfEightBySir(num1)
	elif ch==2:
		isMultipleOf32(num1)

if __name__=='__main__':
	main()
	
	
'''
	****output****
	
	mangesh@mangesh-VPCEH35EN:~/10th Python Batch/program in class$ python3 isMultiple.py 
Enter the number :16
Multiple of 8
mangesh@mangesh-VPCEH35EN:~/10th Python Batch/program in class$ python3 isMultiple.py 
Enter the number :32
Multiple of 8
mangesh@mangesh-VPCEH35EN:~/10th Python Batch/program in class$ python3 isMultiple.py 
Enter the number :31
not multiple
mangesh@mangesh-VPCEH35EN:~/10th Python Batch/program in class$ python3 isMultiple.py 
Enter the number :65  
not multiple
mangesh@mangesh-VPCEH35EN:~/10th Python Batch/program in class$ python3 isMultiple.py 
Enter the number :64
Multiple of 8

'''
