import random

def Consume():
	while True:
		data=yield
		print("Received:{}".format(data))

def Produce(consumer):
	while True:
		data=random.randint(0,1000)
		print("Sent:{}".format(data))
		consumer.send(data)
		yield

if __name__=='__main__':
	consumer=Consume()
	consumer.send(None) #this require to initilize the yield method in Consume() method because here yield in on right side and we are assingning the value of yield in data hence need to initialize it
	producer=Produce(consumer)

	for _ in range(3):
		next(producer)
