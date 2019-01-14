#!/usr/bin/python

class AutoGenerator:
	def __init__(self,start,end,step=1):
		self.start=start
		self.end=end
		self.step=step

	def __next__(self): # doiing this to make program both 2.x and 3.x compatible because 3.x need __next__() method instead of only next() method
		self.start+=self.step
		if self.start >= self.end:
			raise StopIteration
		return self.start
	def next(self):
		return self.__next__()
	def __iter__(self):
		return self

def main():
	x=AutoGenerator(0,100,5) #by creating object and applying for loop we use operator as iterator 
	for y in x:
		print(y)

if __name__=='__main__':
	main()

'''
	z=iter(x)
	print next(z)
	print next(z)
	print next(z)
'''
