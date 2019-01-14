def ToPrintDictionary(input_str):

	i=0
	result_dict={}
	while i < len(input_str):
		if input_str[i] in result_dict:
			result_dict[input_str[i]]=result_dict[input_str[i]]+1
		else:
			result_dict[input_str[i]]=1
		i+=1
	print(result_dict)

def CountOccuranceAndPrintCount(input_str):

    '''    
    count=0
    first_char=input_str[1]
    print(first_char)
    while (len(input_str)!=0):
        for x in input_str:
            if first_char==input_str[x]:
                count=count+1
                print(count)
            else:
                first_char=input_str[x]  
    '''

    i=0
    result_str=""
    while i<len(input_str):
        char_to_check=input_str[i]
        count=1
        while(i+1<len(input_str) and input_str[i+1] == char_to_check):
            count+=1
            i+=1
        result_str+=char_to_check+str(count)
        i+=1
    return result_str


def main():

	input_str=eval(input("Enter the string :"))

	result=CountOccuranceAndPrintCount(input_str)

	print(result)

	input_str=eval(input("Enter the string :"))
	
	ToPrintDictionary(input_str)

if __name__=='__main__':
    main()
