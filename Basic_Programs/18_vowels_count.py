
#WAP to count the vowels and consonent in string

#!/usr/bin/python

def VowelCount(str1):
	vowelCount=0
	consonentCount=0
	for char in str1:
		if char in 'aeiou':
			vowelCount=vowelCount+1
		else:
			consonentCount=consonentCount+1
	print("count of vowel in string is :",vowelCount)
	print("count of consonent in string is :",consonentCount)

def main():
	
	str1=eval(input("Enter the String -:"))

	VowelCount(str1)


if __name__=='__main__':
	main()



'''
	********output********
mangesh@mangesh-VPCEH35EN:~/10th Python Batch/Basic Programs$ python3 18_vowels_count.py 
Enter the String -:"mangesh"
count of vowel in string is : 2
count of consonent in string is : 5
'''
