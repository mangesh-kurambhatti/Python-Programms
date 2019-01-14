def CharacterCountDictionary(input_str):
	result_dict={}
	i=0
	count=1
	while i < len(input_str):
		count=1
		char_to_check=input_str[i]
		if char_to_check in result_dict:
			while i+1<len(input_str) and input_str[i+1]==char_to_check:
				count+=1
				i+=1
			result_dict[input_str[i]]+=result_dict[input_str[i]]+1
			i+=1
		else:
			result_dict[input_str[i]]=1	
	print(result_dict)		
def main():
	
	input_str=eval(input("\n Enter the string:"))

	CharacterCountDictionary(input_str)
	
	
if __name__=='__main__':
	main()
