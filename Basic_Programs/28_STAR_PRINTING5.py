'''
	WAP to print
	
		A
	   BAB
	  CBABC
	 DCBABCD
'''
def main():
	row=eval(input("Enter the no of rows-:"))
	
	for i in range(0,row):
		for j in range(1,row-i):
			print(" ",end=''),
		for k in range(65+i,65,-1):
			print(chr(k),end=''),
		for l in range(65,65+i+1):
			print(chr(l),end=''),
		print(" ")
if __name__=='__main__':
	main()	




'''
	**********output********

	mangesh@mangesh-VPCEH35EN:~/10th Python Batch/Basic Programs$ python3 28_STAR_PRINTING5.py 
Enter the no of rows-:5
    A 
   BAB 
  CBABC 
 DCBABCD 
EDCBABCDE 


'''
