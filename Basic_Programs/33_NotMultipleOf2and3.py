'''
	WAP to accept a range from user and display or print all the no in the range which are not multiple of 2 & 3

'''
def NotMultipleOf2and3(lwb,upb):
	for x in range(lwb,upb):
		if x%2==0 or x%3==0:
			continue
		print(x)


def main():

	lwb,upb=eval(input("Enter lower and upper bound :"))

	NotMultipleOf2and3(lwb,upb)

if __name__=='__main__':
	main()


'''
	*******output*******

	ipleOf2and3.py 
Enter lower and upper bound :10,30
11
13
17
19
23
25
29

'''
