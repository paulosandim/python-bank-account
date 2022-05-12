

class Account:
    
    def __init__(self, number, owner, balance, limit_account):
        print("Construct object ... {}".format(self))
        self.__number = number
        self.__owner = owner
        self.__balance = balance
        self.__limit_account = limit_account
        
        
    def statement(self):
        print("Statement {} of owner {}".format(self.__balance, self.__owner))
        
    def deposit(self, value_account):
        self.__balance += value_account
        
    def withdraw(self, value_account):
        self.__balance += value_account
        
    def transfer(self, value_account, destiny):
        self.withdraw(value_account)
        destiny.deposit(value_account)
        
    def get_balance(self):
        return self.__balance
    
    def get_owner(self):
        return self.__owner
    
    @property
    def limit_account(self):
        return self.__limit_account
    
    @limit_account.setter
    def limit_account(self, limit_account):
        self.__limit_account = limit_account
    
    
    