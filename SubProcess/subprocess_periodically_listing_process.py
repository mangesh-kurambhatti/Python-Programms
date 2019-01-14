import subprocess
import time

count=0
while(count <= 10):
	x=subprocess.call(["ps", "-A"])
	count+=1
	print(x)
	time.sleep(5)	
#time.sleep(5)
	
