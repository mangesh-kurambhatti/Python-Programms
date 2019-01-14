class stack:
	
	def __init__(self,size=10):
		self.STACK=[]
		self.size=size
	
	def __del__(self):
		del self.stack
	
	def push(self,value):
		self.STACK.append(value)

	def Pop(self):
		return self.STACK.pop()

	def IsFull(self):
		return (self.STACK)==self.size

	def IsEmpty(self):
		return self.STACK==[]
def main()

	st=stack()

	print("1.Push")
	print("2.Pop")
	print("3.IsFull")
	print("4.IsEmpty")

	ch=eval(input("\n Enter the choice:"))

	if ch==1:
		push(st,)	
	#show Menu
	#accept choice
	#perform respective operation
	
		st.push(data)
		data=st.pop()	
	print("\n1.push")
	print("\n2.Pop")
	
	

	l1[]
	
if __name__=='__main__':
	main()
