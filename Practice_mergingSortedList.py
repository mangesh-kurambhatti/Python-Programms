def toMerge(input_list,input_list1):
	l3=[]
	i=0
	j=0
	while i<len(input_list) and j<len(input_list1):
		if input_list[i] > input_list1[j]:
			l3.append(input_list1[j])
			j+=1
		else:
			l3.append(input_list[i])
			i+=1

	if i <len(input_list):
		l3.extend(input_list[i:])
	if j <len(input_list1):
		l3.extend(input_list1[j:])
		
	return l3


def toSort(input_list):
	
	for i in range(0,len(input_list)):
		for j in range(i+1,len(input_list)):
			if input_list[i]>input_list[j]:
				temp=input_list[i]
				input_list[i]=input_list[j]
				input_list[j]=temp

def main():

	input_list=[]
	input_list=eval(input("Enter the list element :"))

	input_list=list(input_list)
	
	toSort(input_list)
	
	print(input_list)
	
	input_list1=[]
	input_list1=eval(input("Enter the list element :"))

	input_list1=list(input_list1)
	
	toSort(input_list1)
	
	print(input_list1)
	
	result=toMerge(input_list,input_list1)
	
	print("Merge List is: {}".format(result))
	
if __name__=='__main__':
	main()
