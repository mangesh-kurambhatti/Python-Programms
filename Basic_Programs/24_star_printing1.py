'''
	WAP to display following pattern	
	*
	**
	***
	****
	*****
'''

def main():
	
	row=input("Enter the no of rows :")

	for x in range(0,row+1):
		for y in range(0,x):
			print("*"),			
			#print('*',end=' ')
		print
if __name__=='__main__':
	main()
