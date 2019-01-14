'''
	WAP
	
	************
	****** *****
	***	    ****
	**	      **
	*		   *	
'''
def main():
	
	row=eval(input("Enter the no of rows:"))

	for i in range(0,row):
		for j in range(i,row):
			print("*",end=''),
		for l in range(0,):
			print(" ",end=''),
		for m in range(0,row-i):
			print("*",end=''),
		print(" ")

if __name__=='__main__':
	main()
