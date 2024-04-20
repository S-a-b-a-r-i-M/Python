"""
THIS RULE STATES IT'LL BE CLEANER INSTEAD OF HAVING ONLY ONE GENERAL INTERFACE CLASS,
 TO HAVE INDIVIDUAL PURPOSE INTERFACE CLASSES.BECAUSE EVERY SUB CLASS MAY NOT BE SIMILAR RIGHT
EX: IN THE O/C PRINCIPLE WE HAVE CREATED A PaymentProcessor INTERFACE FOR EVERY SUB PAYMENT CLASSES
    NOW I WANT TO ADD sms_auth() METHOD IN PAYMENT CLASSES EXCEPT PayPalPayment
    LET SEE HOW CAN WE DO THAT IN USING THIS PRINCIPLE
"""
#  NOTE:** WE CAN USE COMPOSITION **

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


class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, order: Order):
        pass


class Auth_SMS(PaymentProcessor):
    @abstractmethod
    def sms_auth(self, security_code: str):
        pass


class DebitPayment(Auth_SMS):
    def __init__(self):
        self._verified = False

    def sms_auth(self, security_code: str):
        print(f'security code verification starting....')
        if len(security_code) > 10:
            self._verified = True

    def pay(self, order: Order):
        print('debit payment processing')
        if self._verified:
            order.status = 'paid'
            print("payment successful")
        else:
            order.status = 'failed'
            raise Exception('security code is not valid')


class CreditPayment(Auth_SMS):
    def __init__(self):
        self._verified = False

    def sms_auth(self, security_code: str):
        print(f'security code verification starting....')
        if len(security_code) > 10:
            self._verified = True

    def pay(self, order: Order):
        print('credit payment processing')
        if self._verified:
            order.status = 'paid'
            print("payment successful")
        else:
            order.status = 'failed'
            raise Exception('security code is not valid')
        print('credit payment processing')


# IN PAYPAL PAYMENT I No NEED TO ADD SMS AUTH, SO EXTENDS THE PAYMENT PROCESSOR ABSTRACT CLASS INSTEAD OF Auth_SMS
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

# payment = DebitPayment()
# payment.sms_auth('sjfkhsdfhsdafljas')
# payment.pay(obj)

payment = CreditPayment()
payment.sms_auth('sljas')
payment.pay(obj)

# payment = PayPalPayment()
# payment.pay(obj)
