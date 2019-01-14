#!/usr/bin/python

def Print_Odd_No(lwb,upb):
	if(lwb<upb):
		for x in range(lwb,upb):
			if(x&1==0):
				print("{} is even".format(x))
			else:
				print("{} is odd".format(x))
	else:
		print("Please Enter valid input..!")
		return False	
		
def main():
	#lwb=eval(input("Enter the lower bound :"))
	#upb=eval(input("Enter the upper Bound :"))
	lwb,upb=eval(input("Enter the lower bound and upper bound :"))
	Print_Odd_No(lwb,upb)

if __name__=='__main__':
	main()
