"""
ACTUALLY THIS ISN'T A RULE OF SOLID, THIS IS AN ALTERNATE FOR I/S RULE.
LIKE DEFINING A LONG INTERFACE TREE JUST SEPARATE THE DIFFERENT BEHAVIOURS
IN OUR APPLICATION.
FOR EXAMPLE IN I/S RULE WE HAD CRATED TWO INTERFACES (1 PARENT, 1 CHILD)
IN HERE WE ARE GOING TO WRITE ONE SEPARATE CLASS FOR SMS_AUTH
"""

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


# INSTEAD OF CREATING ONE MORE INTERFACE I'VE CREATED AuthSMS CLASS. FOR SEPARATING THE DIFFERENT BEHAVIOUR FROM PAYMENT
class AuthSMS:
    def __init__(self):
        self._verified = False

    def verify(self, security_code: str):
        print('sms auth verification started...')
        if len(security_code) > 10:
            self._verified = True

    def is_valid(self):
        return self._verified


class DebitPayment(PaymentProcessor):
    def __init__(self, authorizer: AuthSMS):
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
    def __init__(self, authorizer: AuthSMS):
        self.authorizer = authorizer

    def pay(self, order: Order):
        print('credit payment processing')
        if self.authorizer.is_valid():
            order.status = 'paid'
            print("payment successful")
        else:
            order.status = 'failed'
            raise Exception('security code is not valid')
        print('credit payment processing')


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

# payment = DebitPayment(sms_auth)
# sms_auth.verify('sjfkhsdfhsdafljas')
# payment.pay(obj)

# payment = CreditPayment(sms_auth)
# sms_auth.verify('sljas')
# payment.pay(obj)

# payment = PayPalPayment()
# payment.pay(obj)
