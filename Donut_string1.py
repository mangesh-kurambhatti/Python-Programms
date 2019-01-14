def String1(num):
	if num<10:
		print("Number of Donut:",num)
	else:
		print("Number of Donut:Many")

def main():
	
	num=eval(input("Enter the no:"))

	String1(num)

if __name__=='__main__':
	main()
