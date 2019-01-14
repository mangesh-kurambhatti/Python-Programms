import sys

def CopyFromOneSourceToDestionationFile(source_file,destination_file):

	src_fd=open(source_file)
	dest_fd=open(destination_file,'a')

	line=src_fd.readline()
	while line != "":
		dest_fd.write(line)
		line=src_fd.readline()	

	src_fd.close()
	dest_fd.close()

def main():
	source_file=sys.argv[1]
	destination_file=sys.argv[2]

	CopyFromOneSourceToDestionationFile(source_file,destination_file)

if __name__=='__main__':
	main()
