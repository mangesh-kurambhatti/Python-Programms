import sys

emp_id=0

def UpdateEmployee(result_dict_info,search_id):
	print("*****Attention******")
	print("Here only marks can be updated as you dont have root access..!")
	
	new_salary=eval(input("Enter the new Salary to be updated in dictionary:"))
	
	if search_id in result_dict_info:
		result_dict_info.values(salary)=new_salary
		
	print(pwd)

def SearchEmployee(result_dict_info,search_id):
	if search_id in result_dict_info:
		print(result_dict_info[search_id])
	else:
		print("record not found\n\n") 

def CreateEmployee(result_dict):
	
	emp_dict={}
	name=eval(input("Enter the name:"))
	dob=eval(input("Enter the DOB:"))
	salary=eval(input("Enter the salary:"))
	
	return emp_insert(emp_dict,result_dict,name,dob,salary)
	
def empRecord(emp_dict,name,dob,salary):
		
	
	emp_dict["name"]=name
	emp_dict["dob"]=dob
	emp_dict["salary"]=salary
	
	return emp_dict

def emp_insert(emp_dict,result_dict,name,dob,salary):
	global emp_id
	emp_id+=1
	
	return_emp_dict=empRecord(emp_dict,name,dob,salary)
	result_dict[emp_id]=return_emp_dict

	return result_dict
	
def main():
	result_dict={}
	result_dict_info={}
	
	while True:
		print("1.Insert Employee")
		print("2.Search Employee")
		print("3.update Employee")	
		print("0.exit\n\n")	
		ch=eval(input("Enter the choice :"))
		if ch==1:
			result_dict_info=CreateEmployee(result_dict)	
			print(result_dict_info)
		if ch==2:
			search_id=eval(input("Enter the id to search employee:"))
			SearchEmployee(result_dict_info,search_id)
		if ch==3:
			search_id=eval(input("Enter the id to search employee:"))	
			UpdateEmployee(result_dict_info,search_id)
		if ch==0:
			sys.exit()	
	

if __name__=='__main__':
	main()
