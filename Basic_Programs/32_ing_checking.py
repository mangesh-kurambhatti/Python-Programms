'''
	WAP to accept string from user if length of string is greater than 3 add "ing" to its end.if "ing" 
	is already then replace that "ing" with "ly" e.g loving->lovly.if length of string is greater than 		3 return as it is
''' 


def verbing(input_str):

	adding_ing="ing"
	#adding_ly="ly"

	if (len(input_str)>3) and (input_str[-3::] != adding_ing):
		return input_str+adding_ing
		#print("string is :",y)
	elif (len(input_str)>3) and (input_str[-3::] == adding_ing):
		return input_str.replace("ing","ly")
		#print("string is :",x)
	else:
		print("Length is less than Three so returning string as it is :",input_str)
def main():

	input_str=eval(input("Enter the string :"))

	output_str=verbing(input_str)
	
	print("Verb of {} is {}".format(input_str,output_str))	

if __name__=='__main__':
	main()

'''
	******output******

	mangesh@mangesh-VPCEH35EN:~/10th Python Batch/Basic Programs$ python3 32_ing_checking.py 
Enter the string :"mangesh"
Verb of mangesh is mangeshing
mangesh@mangesh-VPCEH35EN:~/10th Python Batch/Basic Programs$ python3 32_ing_checking.py 
Enter the string :"add"
Length is less than Three so returning string as it is : add
Verb of add is None
mangesh@mangesh-VPCEH35EN:~/10th Python Batch/Basic Programs$ python3 32_ing_checking.py 
Enter the string :"lovely"
Verb of lovely is lovelying

'''

'''
	********output*********
	mangesh@mangesh-VPCEH35EN:~/10th Python Batch$ python3 ing_checking.py 
Enter the string :"mangesh"
string is : mangeshing
mangesh@mangesh-VPCEH35EN:~/10th Python Batch$ python3 ing_checking.py 
Enter the string :"adding"
string is : ly
mangesh@mangesh-VPCEH35EN:~/10th Python Batch$ python3 ing_checking.py 
Enter the string :"adding"
string is : addly
mangesh@mangesh-VPCEH35EN:~/10th Python Batch$ python3 ing_checking.py 
Enter the string :"add"
Length is less than Three so returning string as it is : add


'''

	
