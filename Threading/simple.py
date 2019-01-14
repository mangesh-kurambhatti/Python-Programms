import threading
import time


def worker(name):

	time.sleep(2)
	print("Worker:"+name)
	print(threading.currentThread().getName())
if __name__=='__main__':
	t=threading.Thread(target=worker,args=("mangesh",),name="Interesting")
	t.start()
	t.join()

	for i in range(10):
		time.sleep(1)
		print(i)
