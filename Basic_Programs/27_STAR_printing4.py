'''
	WAP
			*
		   ***
		  *****
'''
def main():
	

	'''
	for i in range(1,row+1):
		for j in range(0,row-i):
			print (" ", end=''),
		for k in range(0,(2*i-1)):
			print ("*",end='')
		print(" ")
	'''

	row=eval(input("Enter the no of rows:"))
	for i in range(1,row+1):
		for j in range(0,row-i):
			print(" ",end=''),
		for k in range(0,(2*i-1)):
			print("*",end=''),
		print(" ")

if __name__=='__main__':
	main()
