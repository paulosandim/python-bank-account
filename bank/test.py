

def creat_account(number, owner, balance, limit_account):
    account = {"number": number, "owner account": owner, "balance": balance, "limit account": limit_account}
    return account

def deposit(account, value_account):
    account["balance"] += value_account

def withdraw(account, value_account):
    account["balance"] -= value_account

def statement(account):
    print("Your balance is {}".format(account["balance"]))