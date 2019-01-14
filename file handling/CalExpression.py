# calculate the expresiion if user h 5 then ans=5+55+555+5555


def CalExpression(num):
	result=0
	num1=num
	count=1
	while count<=num:
		result+=num1+num*10+num1
		count+=1

	print(result)



def main():
	num=eval(input("\n Enter the number:"))

	CalExpression(num)

if __name__=='__main__':
	main() 
