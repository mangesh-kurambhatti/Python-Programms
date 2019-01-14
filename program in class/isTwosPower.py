

def isTwosPower(num1):
	x=1
	count=0
	while(x<=num1):
		if (num1 & x)!=0:
			count+=1
		x=x<<1	
		
	if count==1:
		print("2s Power..!")
  	
'''def RightMostBitTurnOff(num1):
	x=1
	if(num1!=0):
		while(x):
			if(num1 & x):
				break;
			else:
				x=x<<1
	result=num1 & ~x
	print("result is:",result)		 
'''
def main():

	num1=eval(input("Enter the no:"))
	
	isTwosPower(num1)

	RightMostBitTurnOff(num1)
if __name__=='__main__':
	main()
