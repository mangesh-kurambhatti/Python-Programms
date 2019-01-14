def ReadLineDemo(file_name):
	i=0
	key_list=[]
	result_dict={}
	fd=open(file_name)
	line=fd.readline()
	while line != "":
		print(line)
		line=fd.readline()
def main():

	file_name=input("Enter the file name from current directory:")
	
	ReadLineDemo(file_name)

if __name__=='__main__':
	main()
