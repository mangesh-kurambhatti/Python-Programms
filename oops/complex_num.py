class complex:
	def __init__(self,real=0,imag=0):
		self.iReal=real
		self.iImag=imag

	def __add__(self,number):#overloaded __add__ like we do str1+str2 or l1+l2
		result=complex()		

		if isinstance(number,complex):

			result.iReal=self.iReal+number.iReal
			result.iImag=self.iImag+number.iImag

	  	elif isinstance(number,int):
			result.number=self.number+number.number

		else:
			print("No is of another type please provide the valid input..!")
			
		#__repr__ to print the content of object 
		#if we do (print c2 ) -->c2 is object 
		#to print the content of object we have to overload the __repr__ method.
		#def __repr__(self):
			#return str((self.iReal)+str(self.iImag)+"i"
