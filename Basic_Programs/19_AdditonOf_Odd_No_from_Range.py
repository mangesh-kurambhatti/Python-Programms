# WAP TO ACCEPT RANGE FROM USER AND PRINT THE ADDITON OF ODD NUMBER FROM THAT RANGE

#!/usr/bin/python

def AdditonOfOddNos(lbd,ubd):
	OddSum=0
	for x in range(lbd,ubd+1):
		if(x&1):
			OddSum=OddSum+x
		
	print("Addition of odd no from range {} to {} is:{}".format(lbd,ubd,OddSum))			

def main():
	lbd,ubd=eval(input("Enter the lower bound and upper bound :"))

	AdditonOfOddNos(lbd,ubd)

if __name__=='__main__':
	main()


'''
	*******output********
	
	mangesh@mangesh-VPCEH35EN:~/10th Python Batch/Basic Programs$ python3 19_AdditonOf_Odd_No_from_Range.py 
Enter the lower bound and upper bound :1,10
Addition of odd no from range 1 to 10 is:25
'''
