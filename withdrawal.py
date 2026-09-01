#Bank Withdrawal

Balance = 50000
Withdrawal_amount = int(input("Enter the Withdrawal amount"))

if Balance == 0 or Balance <0:
    print("Invalid amount")
elif Withdrawal_amount > Balance:
    print("Insufficient Balance in your account")
elif Withdrawal_amount == Balance:
    print("Invalid Request, Account should have the minimum balance of Rs500")
elif Withdrawal_amount%100 !=0:
    print("Enter the amount in multiple of 100")
else:
    print("Amount of "+str(Withdrawal_amount)+" is successful")
    Balance-=Withdrawal_amount
    print("Balance",Balance)

