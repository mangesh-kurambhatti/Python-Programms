#!/usr/bin/python

num1=eval(input("Enter the 1st no:"))

num2=eval(input("Enter the 2nd no:"))

num3=eval(input("Enter the 3rd no:"))


if (num1<num2)and(num1<num3):
	print("First no is Minimum: ",num1)
elif (num2<num3):
	print("Second no is Minimum: ",num2)
else:
	print("Third no is Minimum: ",num3)


'''
	output-:
	mangesh@mangesh-VPCEH35EN:~/10th Python Batch/Basic Programs$ python3 11_MinThreeNo.py 
	Enter the 1st no:34
	Enter the 2nd no:23
	Enter the 3rd no:78
	Second no is Minimum:  23
'''
