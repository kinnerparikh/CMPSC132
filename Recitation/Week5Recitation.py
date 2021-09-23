class Account: 
   def __init__(self, acct_holder): 
        """Initial account balance is 0 and holder is acct_holder"""
        self._holder = acct_holder
        self._balance = 0
   def deposit(self, amount): 
        """Increment account balance by amount and return new balance"""
        self._balance += amount
   def withdraw(self, amount): 
        """Decrement account balance by amount and return amount withdrawn. Overdraft is not allowed"""
        if amount <= self._balance:
            self._balance -= amount
   @property
   def get_balance(self): 
        """Return account's balance"""
        return self._balance

class CheckingAccount(Account):
    def __init__(self, acct_holder): 
        """Initial account balance is 0 and holder is acct_holder"""
        super().__init__(acct_holder)  # To initialize attributes from the base case
        self._overdraft = False
    def deposit(self, amount): 
        """Increment account balance by amount and return new balance"""
        Account.deposit(self, amount)
        if self._balance >= 0:
            self._overdraft = False
            
    def withdraw(self, amount): 
        """Decrement account balance by amount and return amount withdrawn. Overdraft is allowed once"""
        if not self._overdraft:
            self._balance -= amount
            if amount > self._balance:
                self._overdraft = True
        else:
            return 'Account is overdraft'

help(CheckingAccount)