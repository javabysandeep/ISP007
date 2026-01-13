from functools import singledispatch


class PaymentMode:
    def __init__(self, payment_mode):
        self.payment_mode = payment_mode


class Payment:

    def __init__(self, account_holder_name, account_holder_balance):
        self.account_holder_name = account_holder_name
        self.account_holder_balance = account_holder_balance

    @singledispatch
    def payment(method):
        raise

    def process_payment(self, payment_mode):
        print("process payment using UPI")

    def process_payment(self, payment_mode):
        print("process payment using Credit Card")

    def process_payment(self, payment_mode):
        print("process payment using Debit Card")




payment_mode = PaymentMode('UPI')
upi = Payment('shubham', 1000)
upi.process_payment(payment_mode)
