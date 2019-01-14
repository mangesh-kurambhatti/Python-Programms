def	DictionaryFromFileWithAllScenarioHandle(filename):
	final_dict={}
	result_dict={}
	fd=open(filename)
	line=fd.readline()
	while line !="":
		if line.startswith("["):
			if not line.startswith("#") and "=" in line:
				l1=line.split("=")
				value=l1[1]
				if "#" in l1[1]:
					value=l1[1].split("#")[0]
				result_dict[l1[0]]=value.strip() #this removes \n \t from values hence strip() is used
		line=fd.readline()
		else:
			
	print(result_dict)

def SimpleDictionaryFromDemoFile(file_name):
	result_dict={}
	fd=open(file_name)
	line=fd.readline()
	while line != "":
		if "=" in line:
			l1=line.split("=")  #-----this will give as list->['HFP','TRUE'] hence l1[0]=HFP and l1[1]=true   
			result_dict[l1[0]]=l1[1]
			line=fd.readline()
	print(result_dict)

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
	
	#ReadLineDemo(file_name) 

	SimpleDictionaryFromDemoFile(file_name) #here enter demo txt file
	
	filename=input("Enter the file name:")
	
	DictionaryFromFileWithAllScenarioHandle(filename) #here enter  audio.conf file to check all scenario
if __name__=='__main__':
	main()
