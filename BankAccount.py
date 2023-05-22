class BankAccount:
    
    bank_name = "Iron Bank of Braavos"
    all_accounts = []

    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance


    def deposit(self, d_amount):
        self.balance += d_amount
        return self

    def withdraw(self, w_amount):
        if(self.balance - w_amount) >= 0:
            self.balance -= w_amount
        else:
            print('Insufficient Funds: Charging a 5 Gold Dragon Coin Fee')
            self.balance -= 5
        return self

    def display_account_info(self):
        print(f'{BankAccount.bank_name}, Annual Interest Rate: {self.int_rate * 100} %, Gold Dragon Balance: {self.balance}')
        return self

    def yield_interest(self):
        account_yield = self.balance * self.int_rate;
        self.balance += account_yield
        print ('Your annual account interest yield is: ',account_yield)
        return self

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self 




Tyrions_Account = BankAccount(0.03, 1000.00)

Cerseis_Account = BankAccount(0.0375, 10000)

Tyrions_Account.deposit(1000).deposit(3000).deposit(5000).withdraw(1000).yield_interest().display_account_info()

Cerseis_Account.deposit(7000).deposit(10000).withdraw(2000).withdraw(1000).withdraw(500).withdraw(1000).yield_interest().display_account_info()