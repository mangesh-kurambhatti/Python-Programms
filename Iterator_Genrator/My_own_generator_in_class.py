
class AutoGenerator():
	
	def __init__(self,start,end,step=1):
		self.start=start
		self.end=end
		self.step=step
	'''
	def __next__(self):
		self.start+=self.step
		if self.start >= self.end:
			raise StopeIteration
		yield self.start

	def next(self):
		return self.__next__()

	def __iter__(self):
		return self

	'''
	def Next(self):
		self.start+=self.step
		if self.start >= self.end:
			raise StopeIteration
		yield self.start

	def next(self):
		return self.Next().next()
	
	def __next__(self):
		 return self.Next().__next__()

	def __iter__(self):
		return self
	
def main():

	x=AutoGenerator(0,100,5)
	'''	
	y=x.next()
	print(y)
	print(next(y))

	y=x.next()
	print(y)	
	print(next(y))
	#print(next(y))
	'''

	#for y in x:  # if using for loop then iteraor is import we cant comment it
		#print(y.next())

	print(type(x))
	y=x.next()
	print(y)
	y=x.next()
	print(y)
	
if __name__=='__main__':

	main()
