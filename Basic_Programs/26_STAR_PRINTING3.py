'''
	WAP to print
	
	A
	AB
	ABC
	ABCD
'''
#!/usr/bin/python

def main():
	
	row=input("Enter the no of rows: ")

			
	for x in range(0,row):
		for y in range(65,65+x):
			#ch=str(y)
			print(chr(y)),			
		print

if __name__=='__main__':
	main()	
