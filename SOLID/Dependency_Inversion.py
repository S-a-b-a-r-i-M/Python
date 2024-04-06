"""
THIS RULE STATES THAT METHOD OR CLASSES SHOULD BE DEPENDED ON ABSTRACT SUBCLASSES NOT ON CONCRETE CLASSES.
IN Composition OUR CLASS DEPENDS ON THE AuthSMS CLASS RIGHT, WHAT IF I WANT TO ADD AuthEmail IN THE FUTURE,
IN THAT CASE I NEED TO CHANGE SOME IMPLEMENTATIONS IN THOSE CLASSES WHICH USING THE AuthSMS.
LET SEE WHAT THIS RULE GONNA OVERCOME THIS ISSUE,
"""
import re
from abc import ABC, abstractmethod


class Order:

    def __init__(self):
        self.names = []
        self.quantities = []
        self.prices = []
        self.status = 'open'

    def add_item(self, name: str, quantity: int, price: float):
        self.names.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def total_price(self):
        total = 0
        for i in range(len(self.prices)):
            total += self.prices[i] * self.quantities[i]

        return total

    def is_item_available(self, name: str):
        pass


class Authorizer(ABC):
    name = None

    @abstractmethod
    def is_valid(self):
        pass


class AuthSMS(Authorizer):
    def __init__(self):
        self._verified = False

    def verify(self, security_code: str):
        print('sms auth verification started...')
        if len(security_code) > 10:
            self._verified = True

    def is_valid(self):
        return self._verified


class AuthEmail(Authorizer):
    def __init__(self):
        self._verified = False

    def verify(self, email: str):
        print('email auth verification started...')
        # Regular expression pattern for validating email addresses
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

        # Use re.match() to check if the email matches the pattern
        if bool(re.match(pattern, email)):
            self._verified = True

    def is_valid(self):
        return self._verified


class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, order: Order):
        pass


class DebitPayment(PaymentProcessor):
    def __init__(self, authorizer: Authorizer):
        self.authorizer = authorizer

    def pay(self, order: Order):
        print('debit payment processing')
        if self.authorizer.is_valid():
            order.status = 'paid'
            print("payment successful")
        else:
            order.status = 'failed'
            raise Exception('security code is not valid')


class CreditPayment(PaymentProcessor):
    def __init__(self, authorizer: Authorizer):
        self.authorizer = authorizer

    def pay(self, order: Order):
        print('credit payment processing')
        if self.authorizer.is_valid():
            order.status = 'paid'
            print("payment successful")
        else:
            order.status = 'failed'
            raise Exception('security code is not valid')


class PayPalPayment(PaymentProcessor):
    def pay(self, order: Order):
        print('paypal payment processing')
        order.status = 'paid'
        print("payment successful")


obj = Order()
obj.add_item('vivo', 1, 10000)
obj.add_item('bat', 2, 1000)
obj.add_item('face cream', 2, 499)
print("Total price:", obj.total_price())

sms_auth = AuthSMS()
email_auth = AuthEmail()

# payment = DebitPayment(sms_auth)
# sms_auth.verify('sjfkhsdfhsdafljas')
# payment.pay(obj)

payment = CreditPayment(email_auth)
email_auth.verify('sabarinithi2002@gmail.com')
payment.pay(obj)

# payment = PayPalPayment()
# payment.pay(obj)
