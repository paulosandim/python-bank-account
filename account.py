

class Account:
    
    def __init__(self, number, owner, balance, limit_account):
        print("Construct object ... {}".format(self))
        self.number = number
        self.owner = owner
        self.balance = balance
        self.limit_account = limit_account
        
        
    def statement(self):
        print("Statement {} of owner {}".format(self.balance, self.owner))