import sys

def CountExactNoOfZerosandOne(num1,num2):
		
	result1=CountTheNoOfOneInNumber(num1)
	result2=CountTheNoOfOneInNumber(num2)	
	
	if(result1==result2):
		print("have same no of one bit and zero bit")
	else:
		print("not same")

def ToggleBit(num,position,bits):

	x=(1<<bits)-1
	x=x<<(position-bits)
	result=num^x
	
	print("\nRESULT IS:\n",result,"\n")
		
	
def TurnOnRespectiveBitsFromRespectivePosition(num,position,bits):
	x=(1<<bits)-1
	x=x<<(position-bits)
	result=num|x
	
	print("\nRESULT IS:\n",result,"\n")
	#print("result is:",result)
	
def TurnOffRespectiveBitsFromRespectivePosition(num,position,bits):
	x=(1<<bits)-1
	x=x<<(position-bits)
	x=~x
	result=num&x
	print("\nRESULT IS:\n",result,"\n")
	#print("result is:",result)

def RightMostBitTurnOff(num1):
	x=1
	if(num1!=0):
		while(x):
			if(num1 & x):
				break;
			else:
				x=x<<1
	result=num1 & ~x
	print("\nRESULT IS:\n",result,"\n")
	#print("result is:",result)		 


def isTwosPower(num1):
	x=1
	count=0
	while(x<=num1):
		if (num1 & x)!=0:
			count+=1
		x=x<<1	
		
	if count==1:
		print("2s Power..!")


def CountTheNoOfOneInNumber(num):
	x=1
	count=0
	while(x<=num):
		if (num & x)!=0:
			count+=1
		x=x<<1	
	return count
def main():
	
	while True:
		print("1.Count the number of 1 bit in number")
		print("2.To check whether no is 2s power or not..!")
		print("3.To TurnOff the Rigt most 1st bit")
		print("4.To Turnoff the Respective Bits from given position")
		print("5.To TurnOn the Respective Bits from given position")
		print("6.To Toggle the respective bits")
		print("7.To check no containing exactly same no of 0 and 1")
		print("0.exit")	
		ch=eval(input("Enter your choice:"))
	
		if ch==1:
			num=eval(input("Enter the number:"))
			result=CountTheNoOfOneInNumber(num)
			print("count of 1 bit is:",result)
		elif ch==2:
			num1=eval(input("Enter the number:"))
			isTwosPower(num1)
		elif ch==3:
			num1=eval(input("Enter the number:"))
			RightMostBitTurnOff(num1)
		elif ch==4:
			num=eval(input("Enter the number:"))
			position=eval(input("Enter the position:"))
			bits=eval(input("Enter the no of bits:"))
			
			TurnOffRespectiveBitsFromRespectivePosition(num,position,bits)
		elif ch==5:
			num=eval(input("Enter the number:"))
			position=eval(input("Enter the position:"))
			bits=eval(input("Enter the no of bits:"))
			
			TurnOnRespectiveBitsFromRespectivePosition(num,position,bits)
		
		elif ch==6:
			num=eval(input("Enter the number:"))
			position=eval(input("Enter the position:"))
			bits=eval(input("Enter the no of bits:"))
			
			ToggleBit(num,position,bits)
		elif ch==7:
			num1=eval(input("Enter the number 1:"))
			num2=eval(input("Enter the number 2:"))

			CountExactNoOfZerosandOne(num1,num2)
		elif ch==0:
			sys.exit()

if __name__=='__main__':
	main()
