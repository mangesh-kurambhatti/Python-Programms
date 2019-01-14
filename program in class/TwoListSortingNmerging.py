def Merging(l1,l2):
	l3=[]
	i=0	
	j=0
	while i < len(l1) and j<len(l2):
		if l1[i]<l2[j]:
			l3.append(l1[i])
			i+=1
		else:
			l3.append(l2[j])	
			j+=1

	if i<len(l1):
		l3.extend(l1[i:])
	if j<len(l2):
		l3.extend(l2[j:])
		
	return l3
	
	
def Sorting(l1):
	for i in range(len(l1)): #get index from 0,1,2,3,4
		for j in range(i+1,len(l1)):
			if l1[i] > l1[j]:
				temp=l1[i]
				l1[i]=l1[j]
				l1[j]=temp


def main():

	l1=[5,4,3,2]
	l2=[1,8,6,7]
	
	#l3=[]
	#for x in 
	#l3=eval(input("Enter the list..:"))
	
	#l3=list(l3)
	#print(type(l3))
	Sorting(l1)
	Sorting(l2)
	
	print("Sorted lists are:\n list1={} \n list2={}\n".format(l1,l2) )

	result=Merging(l1,l2)
	
	print("After Merging Two Sorted list is:{}".format(result))
if __name__=='__main__':
	main()
