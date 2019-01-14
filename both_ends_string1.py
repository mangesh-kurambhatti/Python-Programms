def both_ends(str1):

	first_two=str1[:2:]
	last_two=str1[-2::]

	combine_str=first_two+last_two
	print("output is :",combine_str)

def main():

	str1=eval(input("Enter the string :"))
	
	both_ends(str1)

if __name__=='__main__':
	main()
