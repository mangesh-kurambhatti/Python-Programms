def mix_up(str1,str2):
	
	first_two_str1=str1[:2:]
	first_two_str2=str2[:2:]

	print("string is:",first_two_str2+str1[2::])
	print("string is:",first_two_str1+str2[2::])
def main():
	
	str1=eval(input("Enter the string1 :"))
	str2=eval(input("Enter the string2 :"))

	mix_up(str1,str2)

if __name__=='__main__':
	main()
