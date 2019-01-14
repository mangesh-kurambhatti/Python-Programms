def addition(a,b,c=0,d=0,e=0):
	return a+b+c+d+e


def main():

	print("Addition is :",addition(10,20))
	print("Addition is :",addition(10,20,30))
	print("Addition is :",addition(10,20,5,5))
	print("Addition is :",addition(10,20,5,5,5))

if __name__=='__main__':
	main()
