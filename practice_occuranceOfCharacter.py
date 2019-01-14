def CountOccuranceOfChar(string):
	
	i=0
	result_str=""
	while i < len(string):
		
		first_char=string[i]
		count=1
		while i+1<len(string) and string[i+1]==first_char:
			count+=1
			i+=1
		result_str+=first_char+str(count)
		i=i+1
	return result_str

def main():
	
	string=eval(input("Enter the string:"))
	
	result=CountOccuranceOfChar(string)

	print(result)
if __name__=='__main__':
	main()
