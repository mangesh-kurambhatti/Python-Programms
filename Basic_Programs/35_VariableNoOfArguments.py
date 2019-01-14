def VariableNoOfArguments(*args):
	print(type(args))
	for x in args:
		print(x)

def main():
	VariableNoOfArguments(1,2,3,4)
	VariableNoOfArguments(1,2,3,4,"i","bye")
if __name__=='__main__':
	main()
