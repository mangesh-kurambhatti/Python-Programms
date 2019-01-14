'''
				 Write a program to accept 2 strings from user. And check if second string is a right rotation of first string.
				Hint:
				India, iaInd -> This should be true
				Jeetendra 1st right rotation "aJeetendr"
						  2nd right rotation "raJeetend"
'''
#!/usr/bin/python

def isRightRotation(str1,str2):
	str3=str1+str2
	if str2 in str3:
		print(" '{}' is right rotation of '{}' ".format(str2,str1))
	else:
		print(" '{}' is  not right rotation of '{}' ".format(str2,str1))
def main():
	
	str1=eval(input("Enter the 1st String :"))
	str2=eval(input("Enter the 2nd String :"))

	isRightRotation(str1,str2)

if __name__=='__main__':
	main()


'''
	*********output**********

	mangesh@mangesh-VPCEH35EN:~/10th Python Batch/Basic Programs$ python3 13_is_Right_Rotation.py 
Enter the 1st String :"india"
Enter the 2nd String :"iaind"
iaind is right rotation of india
mangesh@mangesh-VPCEH35EN:~/10th Python Batch/Basic Programs$ python3 13_is_Right_Rotation.py 
Enter the 1st String :"Jeetendra"
Enter the 2nd String :"raJeetend"
 'raJeetend' is right rotation of 'Jeetendra' 

'''
