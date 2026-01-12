class BankAccount:
    def __init__(self, account_holder_name, account_holder_address, balance):
        self.balance = balance
        self.account_holder_name = account_holder_name
        self.account_holder_address = account_holder_address

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        self.balance = self.balance - amount

    def print(self):
        print(
            'BankAccount[ account_holder_name={},account_holder_address={},balance={}]'.format(self.account_holder_name,
                                                                                               self.account_holder_address,
                                                                                               self.balance))


b1 = BankAccount('shubham', 'pune', 10000)
b2 = BankAccount('swagat', 'mumbai', 11000)
b1.print()
b2.print()
