#!/usr/bin/python
import math

def IsPrime(number):
    retVal = False
    if number > 1:
        if number == 2:
            retVal = True
        if not number & 1:
            retVal = False
        else:
            for divisor in range(3, int(math.sqrt(number)+1), 2):
                if number % divisor == 0:
                    retVal = False
                    break
            else:
                retVal = True
    return retVal 

def getPrime(inputList):
	for i in inputList:
		if(IsPrime(i)):
			yield i


def main():
	x=getPrime(range(1,40))

	print next(x)
	print next(x)
	print next(x)
	print next(x)
if __name__=='__main__':
	main()
