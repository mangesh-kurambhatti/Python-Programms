from threading import Thread,Event #Event is a class in Threading it allow us to schedule the thread using differt event it a can act as a flag

import time
data=[]
size=0
producer_event=Event()
consumer_event=Event()

def read():
	global data
	global size
	global producer_event
	global consumer_event
	print("Inside Consumer..!")

	while True:
		producer_event.wait()
		
		print("\n Consumed",data[0])
		del data[0]
		size=size-1

		consumer_event.set()
		producer_event.clear()

def write():

	global data
	global size
	global producer_event

	print("In Producer..!")

	while True:
		x=input("Enter Data:")
		data.append(x)
		size=size+1
		#add to queue
		producer_event.set()
		
		#if queue is full consume.wait()

		if data==10:
			consumer_event.wait()
			consumer_event.clear()

consumer=Thread(target=read)
producer=Thread(target=write)
consumer.start()
producer.start()

consumer.join()
producer.join()

print("Done")
