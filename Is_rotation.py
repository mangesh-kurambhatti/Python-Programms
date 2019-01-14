#!/usr/bin/python

def Is_Rotation(input_str,validate_str):
	if len(input_str)==len(validate_str):
		return validate_str in input_str+input_str
	return False
		
def main():
	input_str=input("Enter input string :")
	validate_str=input("Enter the string for validation :")

	if Is_Rotation(input_str,validate_str):
		print("{} is rotation of {}".format(validate_str,input_str))
	else:
		print("{1} is not rotation of {0}".format(input_str,validate_str))

if __name__=='__main__':
	main()
