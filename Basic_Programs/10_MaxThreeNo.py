#!/usr/bin/python

num1=eval(input("Enter the 1st no:"))

num2=eval(input("Enter the 2nd no:"))

num3=eval(input("Enter the 3rd no:"))


if (num1>num2)and(num1>num3):
	print("First no is Maximum: ",num1)
elif (num2>num3):
	print("Second no is Maximun: ",num2)
else:
	print("Third no is Maximum: ",num3)


'''
	output-:
	mangesh@mangesh-VPCEH35EN:~/10th Python Batch/Basic Programs$ python3 10_MaxThreeNo.py 
		Enter the 1st no:34
		Enter the 2nd no:56
		Enter the 3rd no:89
		Third no is Maximum:  89
		mangesh@mangesh-VPCEH35EN:~/10th Python Batch/Basic Programs$ python3 10_MaxThreeNo.py 
		Enter the 1st no:20
		Enter the 2nd no:11
		Enter the 3rd no:12
		First no is Maximum:  20
		mangesh@mangesh-VPCEH35EN:~/10th Python Batch/Basic Programs$ 
'''
