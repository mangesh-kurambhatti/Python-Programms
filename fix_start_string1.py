def fix_start(str1):
	
	first_letter=str1[:1:]
	
	if  first_letter in str1[1::]:
			y=first_letter+str1.replace(first_letter,"*")
	print("string is:",y)

def main():

	str1=eval(input("Enter the string :"))

	fix_start(str1)

if __name__=='__main__':
	main()
