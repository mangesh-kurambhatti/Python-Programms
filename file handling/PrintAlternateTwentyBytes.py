#WAP to print alternate character and IMP use india_pledge file for this to run for better understanding 

def PrintAlternateTwentyBytes(file_name):
	fd=open(file_name)
	line=fd.read(20)
	print("here")
	while line != "":
		print(line)
		fd.seek(20,1)
		print("after seeking")
		line=fd.read(20)

	line=fd.seek(20,0)
	while line != "":
		print(line)
		fd.seek(20,1)
		print("after seeking")
		line=fd.read(20)

def main():
	file_name=input("Enter the file name:")

	PrintAlternateTwentyBytes(file_name)
if __name__=='__main__':
	main()
