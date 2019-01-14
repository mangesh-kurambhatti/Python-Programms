def square(n):
	for i in range(1,n+1):
		yield i*i

def main():
	x=square(5)
	print next(x)
	print next(x)	
	print next(x)
	print next(x)
	print next(x)
	#print next(x)
if __name__=='__main__':
	main()
