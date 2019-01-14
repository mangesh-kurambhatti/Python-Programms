def adder(no):
	def add(number):
		return no+number
	return add

adder_20=adder(20)
adder_10=adder(10)

print(adder_10(100))
print(adder_10(25))

print(adder_20(100))
print(adder_20(25))
