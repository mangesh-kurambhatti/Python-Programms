import sys

def Push(l1,element):
	l1.append(element)
	
def Pop(l1):
	return l1.pop()

def IsFull(l1):
	return len(l1)==10

def IsEmpty(l1):
	return len(l1)==0


def main():

	l1=[]
	while True:
		print("1.Push")
		print("2.Pop")
		print("3.IsFull")
		print("4.IsEmpty")
		print("5.Display")
		print("0.exit")
		
		ch=eval(input("Enter your choice:"))
	
	#	l1=[]
		if ch==1:
			if not IsFull(l1):
				element=eval(input("Enter the Element :"))
				Push(l1,element)
			else:
				print("Stack is full ..!")
			
		elif ch==2:
			if not IsEmpty(l1):
				element=Pop(l1)
				print("Pop Element is :{}".format(element))
			else:
				print("Stack is Empty..!")
	
		elif ch==3:
			if 	IsFull():
				print("Stack is Full")
			else:
				print("Stack is not Full")
	
		elif ch==4:
			if IsEmpty():
				print("List is not Empty")
			else:
				print("List is Empty")
		
		elif ch==5:
			print(l1)
			
		elif ch==0:
			sys.exit()
		
		else:
			print("Invalid Choice..!")

if __name__=='__main__':
	main()
