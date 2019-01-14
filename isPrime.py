#!/usr/bin/python
import math

def isPrime(num):
	if (num%2==0):
		return False
		#print("It is not prime")		
	else:
		for x in range(3,int(math.sqrt(num))+1,2):
			if (num%x==0):
				return True
			else:
				return False
def main():
	num=eval(input("Enter the Number :"))
	if isPrime(num):
		print("no is prime")
	else:
		print("no is not prime")


if __name__=='__main__':
	main()
