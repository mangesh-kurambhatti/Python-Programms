import subprocess

proc=subprocess.Popen(["cat","-"],stdin=subprocess.PIPE,stdout=subprocess.PIPE)
stdout_value=proc.communicate(b"Hello world")[0]
print(stdout_value)

