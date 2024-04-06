"""
THIS RULE STATES - CODE SHOULD OPEN FOR EXTENSION BUT CLOSED FOR MODIFICATION
,BY DOING THIS WE CAN ENSURE THAT WE ARE NOT PRODUCING ANY NEW BUGS IN THE EXISTING CODE.
IN SINGLE RESPONSIBILITY WE HAVE SEPARATED THE PAYMENT FROM ORDER CLASS,
NOW I WANT TO ADD AN 1 MORE PAYMENT METHOD FOR PAYPAL...WHAT CAN I DO IN THIS CASE??
IF I MODIFY THE PAYMENT PROCESSOR CLASS BY ADDING ONE MORE METHOD FOR PAYPAL ,IT'LL VIOLATE THE O/C RULE....
SO THE SOLUTION IS CREATE A PARENT CLASS AS PAYMENT PROCESSOR DEFINE ABSTRACT METHOD USE IT IN THE DERIVED CLASSES,
BY DOING THIS OUR CODE WILL BE OPEN FOR EXTENSION BUT CLOSED FOR MODIFICATION
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
    def pay(self, security_code: str, order: Order):
        pass


class DebitPayment(PaymentProcessor):
    def pay(self, security_code: str, order: Order):
        print('debit payment processing')
        # if verify_security_code()
        print('security code verified', security_code)
        order.status = 'paid'


class CreditPayment(PaymentProcessor):
    def pay(self, security_code: str, order: Order):
        print('credit payment processing')
        # if verify_security_code()
        print('security code verified', security_code)
        order.status = 'paid'


# IF I WANT TO ADD ANOTHER PAYMENT LIKE PAYPAL I CAN CREATE A ONE MORE SUB CLASS FOR PaymentProcessor CLASS
class PayPalPayment(PaymentProcessor):
    def pay(self, security_code: str, order: Order):
        print('paypal payment processing')
        # if verify_security_code()
        print('security code verified', security_code)
        order.status = 'paid'


obj = Order()
obj.add_item('vivo', 1, 10000)
obj.add_item('bat', 2, 1000)
obj.add_item('face cream', 2, 499)
print("Total price:", obj.total_price())

payment = PayPalPayment()
payment.pay('nfafjsdf9yrre4jedgs', obj)
if obj.status == "paid":
    print("payment successful")
