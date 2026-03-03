account_balance=500.00
atm_user =float(input("how much would you like to draw?"))
if atm_user>account_balance:
    print("transaction failed: insufficient funds.")
else:
    account_balance=account_balance-atm_user
    print("transaction successful. your new balance is:",account_balance)
