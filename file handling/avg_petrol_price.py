'''
	 Write code to read a file of petrol prices in Maharashtra, Goa & Karnataka:
	Jan 2015 81 67 84
	Feb 2015 79 66 82
	Mar 2015 78 65 81
	Apr 2015 77 64 80
	...


	Output the average petrol price for each state to an output file named
	petrol_avg_out.txt
'''
def avg_petrol_price(file_name):

	sum_maha_petrol=0
	sum_goa_petrol=0
	sum_karnatak_petrol=0

	fd=open(file_name)
	line=fd.readline()
	
	while line !="":
		l1=line.split(" ")
		sum_maha_petrol+=int(l1[2])
		sum_goa_petrol+=int(l1[3])
		sum_karnatak_petrol+=int(l1[4])

		line=fd.readline()


	print("Avg petrol price in Maharashtra is:{}".format(sum_maha_petrol/12))
	print("Avg petrol price in Goa is:{}".format(sum_goa_petrol/12))
	print("Avg petrol price in Karnatak is:{}".format(sum_karnatak_petrol/12))


def 

def main():

	file_name=input("Enter the input file name :")

	avg_petrol_price(file_name)

if __name__=='__main__':
	main()
