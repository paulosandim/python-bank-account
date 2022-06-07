
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
        
    def __can_withdraw(self, value_for_withdraw):
        value_available = self.__balance + self.__limit_account
        return value_for_withdraw <= value_available
        
    def withdraw(self, value_account):
        if(self.__can_withdraw(value_account)):
            self.__balance -= value_account
        else:
            print("Value {} exceeded limit account".format(value_account))
        
    def transfer(self, value_account, destiny):
        self.withdraw(value_account)
        destiny.deposit(value_account)
    
    @property    
    def balance(self):
        return self.__balance
    
    @property
    def owner(self):
        return self.__owner
    
    @property
    def limit_account(self):
        return self.__limit_account
    
    @limit_account.setter
    def limit_account(self, limit_account):
        self.__limit_account = limit_account
        
    @staticmethod
    def bank_code():
        return "001"
    
    @staticmethod
    def banks_codes():
        return {'BB':'001', 'Caixa':'104', 'Bradesco':'237'}
    
    