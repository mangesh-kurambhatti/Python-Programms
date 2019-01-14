# WAP to accept name of file & display longest and smallest line in it 


def PrintSmallestLineFromFile(file_name):

	fd=open(file_name)
	line=fd.readline()

	min_line=line

	while line != "":
		print("inside while")
#		line=fd.readline()
		if (len(line)<len(min_line)):
			
			min_line=line
#	print("outside while")
	return min_line

def PrintLongestLineFromFile(file_name):

	
	fd=open(file_name)
	line=fd.readline()
	max_line=line

	while line != "":
		line=fd.readline()	
		if (len(line) > len(max_line)):
			max_line=line
	return max_line

def main():
	
	file_name=eval(input("\n Enter the file name:"))

	x=PrintLongestLineFromFile(file_name)

	print("Longest line from file is : \n\n {}".format(x))

	file_name=eval(input("\n Enter the file name:"))

	
	y=PrintSmallestLineFromFile(file_name)

	print("Smallest line from file is : \n\n {}".format(y))

if __name__=='__main__':
	main()
