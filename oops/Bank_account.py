import sys

class bank:
	Account_no=0
	remaining_amount=0
	def __init__(self,initial_amount):
		bank.Account_no=bank.Account_no+1
		print("Account no is:{}".format(bank.Account_no))
		
		self.initial_amount=initial_amount
		print("Initial Amount is:{}".format(self.initial_amount))	

	def Withdraw(self,initial_amount,withdraw_amount):
		
		if(withdraw_amount < initial_amount):
	
			bank.remaining_amount=(initial_amount - withdraw_amount)
			return bank.remaining_amount

		else:
			print("Balance is low..!")
	
	def Deposit(self,deposit_amount):
		
		return (bank.remaining_amount+deposit_amount)
		
	def Check_Balance():
		return bank.remaining_amount

def main():

	while True:

		print("1.Create Account.")
		print("2.Withdraw.")
		print("3.Deposit.")
		print("4.Check Balance.")
		print("0.Exit.")


		ch=eval(input("Enter the choice:"))

		if ch==1:
			b=bank(10000)
			print("\n")
		elif ch==2:
			c=b.Withdraw(10000,5000)
			print("\nWithdraw amount is {}".format(c))
	
		elif ch==3:
			total=b.Deposit(3000)
			print("\nTotal Amount is :{}".format(total))
	
		elif ch==4:
			amount=bank.Check_Balance()
			print("\n Amount is:{}".format(amount))

		elif ch==0:
			sys.exit()
if __name__=='__main__':
	main()
