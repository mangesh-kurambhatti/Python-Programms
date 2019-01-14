def VariableArgsDictionaryDemo(a,b,c,*args,**kwargs):
	print(a,b,c)
	print(type(args))
	for x in args:
		print(x)

	print(type(kwargs)) #using normal code
	for key in kwargs:
		print(key,kwargs[key])
	
	print(type(kwargs)) #using dictionary method "items()"
	for key,value in kwargs.items():
		print(key,value)

def main():
	VariableArgsDictionaryDemo(1,2,3,7,8,9,10,name="mangesh",Hobby="teaching")

if __name__=='__main__':
	main()
