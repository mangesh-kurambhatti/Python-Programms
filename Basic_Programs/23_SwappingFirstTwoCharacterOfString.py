#6. Write a program to accept 2 strings from user and swap 1st 2 characters of each of them.
#e.g. Jeetendra=Bhetendra
#	  Bharat=Jearat



def Swapping(str1,str2):
	
	temp1=str1[:2:]
	temp2=str2[:2:]

	print("After swapping 1st two character of second string with 1st string, first string becomes :",temp2+str1[2::])

	print("After swapping 1st two character of 1st string with 2nd string, second string becomes :",temp1+str2[2::])




def main():
		
	str1=eval(input("Enter the 1st String :"))
	str2=eval(input("Enter the 2nd String :"))

	Swapping(str1,str2)



if __name__=='__main__':
	main()

'''
	**********output********

	mangesh@mangesh-VPCEH35EN:~/10th Python Batch/Basic Programs$ python3 23_SwappingFirstTwoCharacterOfString.py 
Enter the 1st String :"Jeetendra"
Enter the 2nd String :"Bharat"
After swapping 1st two character of second string with 1st string, first string becomes : Bhetendra
After swapping 1st two character of 1st string with 2nd string, second string becomes : Jearat

'''
