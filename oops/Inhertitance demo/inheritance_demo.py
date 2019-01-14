class Base(object):
	
	def bar(self):
		print("Base bar")
	
	def foo(self):
		print("Base foo")

class Derived1(Base):
	
	def bar(self):
		print("Derived1 bar")
	
	 
class Derived2(Base):

		
	def foo(self):
		print("Derived 2 foo")


class Child(Derived1,Derived2):
	pass


def main():
	x=Child()
	x.foo()
	x.bar()

if __name__=='__main__':
	main()
