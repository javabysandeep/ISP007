class BankAccount:
    def __init__(self, account_number, account_holder_name, balance):
        # assigning local variable value to instance variable
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        if self.check_balance() > 0:
            self.balance = self.balance - amount

    def check_balance(self):
        return self.balance

    def print_account_details(self):
        print('Account number = {}, Account holder name = {}, Balance= {}'.
              format(self.account_number,
                     self.account_holder_name,
                     self.balance))


b1 = BankAccount(123, 'Aryan', 1002300)
b2 = BankAccount(124, 'Bhakti', 98999)
b3 = BankAccount(125, 'Madhavi', 51000)
b4 = BankAccount(126, 'Shubham', 89898)

b1.print_account_details()
b2.print_account_details()
b3.print_account_details()
b4.print_account_details()

b1.balance= 2000
