def ReverseDisplay(fd):
	line=fd.readline()
	if line=="":
		return 
	ReverseDisplay(fd)
	print(line)

def main():
	file_name=eval(input("\n Enter the file name :"))
	fd=open(file_name)
	ReverseDisplay(fd)


if __name__=='__main__':
	main()t
