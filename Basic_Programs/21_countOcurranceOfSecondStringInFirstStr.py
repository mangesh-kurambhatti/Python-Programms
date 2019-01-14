#WAP to accept string & a charter or another string and without using count method, count the occurances of #second string into first string.

#!/usr/bin/python

def toCheckOccurance(input_string,occuring_string):
	count=0	
	for char in input_string:	
		if occuring_string == char:
			count=count+1
	print("count of '{}' in '{}' is :{}".format(occuring_string,input_string,count))	
			
def main():
	
	input_string=eval(input("Enter the input string :"))
	occuring_string=eval(input("Enter the string to check the occurance of string in input string:"))

	toCheckOccurance(input_string,occuring_string)

if __name__=='__main__':
	main()

'''
	******output********

mangesh@mangesh-VPCEH35EN:~/10th Python Batch/Basic Programs$ python3 21_countOcurranceOfSecondStringInFirstStr.py 
Enter the input string :"sadsassssssssssdasfsfs"
Enter the string to check the occurance of string in input string:"f"
count of f in sadsassssssssssdasfsfs is :2

'''
