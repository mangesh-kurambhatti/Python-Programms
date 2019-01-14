def ListAppendExtendDemo(l1,element):
	if type(element)==list:
		l1.extend(element)
	else:
		l1.append(element)

	print(l1)
	
def main():
	
	l1=[1,2,3,4,5,6,6,6]

	#ListAppendExtendDemo(l1,5)
		
	#ListAppendExtendDemo(l1,[6,7,8])
	
	l1.pop()
	print(l1)		

	l1.pop(2)
	print(l1)
	
	
	l2=[6,1,2,3,4,5,6,6,6]
	l2.remove(6)
	print(l1)
	
	l3=[1,2,3,4,5]
	l3.reverse()
	print(l3)
	
	
if __name__=='__main__':
	main()
