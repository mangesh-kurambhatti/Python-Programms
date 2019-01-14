class SimpleClass:
	institute_name="Trinha solutions"

	def __init__(self,value):
		self.object_attribute=value
		self.__private_attribute=100
		print("constructor")
	def __del__(self):
		print("Destructor")

	def setAttribute(self,value):
		self.object_attribute=value	
	def getAttribute(self):
		print(id(self))
		#print(id(self))
		return self.object_attribute
	def __setPrivateAttribute(self,value):
		self.__private_attribute=value
		

def main():
	x=SimpleClass(10);
	y=SimpleClass(20);

	print(x.getAttribute())
	print(y.getAttribute())

	print(x.__dict__)

	#print(SimpleClass.__setPrivateAttribute(200))	
	
	print(x._SimpleClass__setPrivateAttribute(200))
	
	#print(SimpleClass.__setPrivateAttribute)
	#print(x.object_attribute)

	#print(SimpleClass.__dict__)
	


	#print(x.__private_attribute)
	
		#print(y.__dict__)

	
	#print(SimpleClass.institute_name)
	
	#x.teach=True
	#print(x.__dict__)
	#print(y.__dict__)
	

	#print(id(x))
	#print(id(y))

if __name__=='__main__':
	main()
