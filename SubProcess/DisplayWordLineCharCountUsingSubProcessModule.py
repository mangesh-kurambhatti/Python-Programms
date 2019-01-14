import subprocess

def DisplayWordLineCharCount():

	fd=open("demo",'r')
	
	ret=subprocess.Popen(["wc","-c"],stdin=fd,stdout=subprocess.PIPE)

	stdout_value=ret.communicate(b'')[0]

	print("Character count={}".format(stdout_value))

	fd=open("demo",'r')

	ret=subprocess.Popen(["wc","-w"],stdin=fd,stdout=subprocess.PIPE)

	stdout_value=ret.communicate()[0]

	print("Word count={}".format(stdout_value))

	fd=open("demo",'r')

	ret=subprocess.Popen(["wc","-l"],stdin=fd,stdout=subprocess.PIPE)

	stdout_value=ret.communicate(b'')[0]

	print("Line count={}".format(stdout_value))

def main():
	
	DisplayWordLineCharCount()

if __name__=='__main__':
	main()
