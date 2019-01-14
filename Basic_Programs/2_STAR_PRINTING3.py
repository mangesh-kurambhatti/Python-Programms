'''
	WAP to print
	
	*****
	 ****
	  ***
	   **
	    *
'''
#!/usr/bin/python
def main():
	
	row=input("Enter the no of rows: ")

			
	for x in range(0,row):
		for y in range(x,row):
			print("*"), 
		print

if __name__=='__main__':
	main()	
