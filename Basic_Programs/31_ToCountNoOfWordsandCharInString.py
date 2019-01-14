'''
	WAP
	accept a string from user print the no of characters words in the given sentence..!
'''

def ToCountNoOfWordsandChar(input_str):

	word_count=0
	char_count=0

	for x in range(0,len(input_str)):
		char_count=char_count+1
					
	print("char count count is :",char_count)

	for x in input_str.split(" "):
		word_count=word_count+1
	print("word count is :",word_count)

def main():

	input_str=eval(input("Enter the string :"))

	ToCountNoOfWordsandChar(input_str)
	

if __name__=='__main__':
	main()


'''
	******output******

	mangesh@mangesh-VPCEH35EN:~/10th Python Batch/Basic Programs$ python3 31_ToCountNoOfWordsandCharInString.py 
Enter the string :"India is my country. I Love My Country"
char count count is : 38
word count is : 8

'''
