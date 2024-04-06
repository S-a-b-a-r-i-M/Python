"""
IN OUR EXAMPLE WE HAVE IMPLEMENTED A ORDER CLASS,
IN THAT,
    DEFINED ADD_ITEM, TOTAL_PRICE, IS_AVAILABLE AND PAYMENT_PROCESS
I HAVE THOUGHT PAYMENT CAN BE SEPARATED BECAUSE WE CAN REUSE IT IN FUTURE 
SO LET'S CREATE A PAYMENT CLASS ADD DEFINE PAYMENT METHODS.
BY DOING THIS, ORDER CLASS HAVE ONLY THE ORDER RELATED RESPONSIBILITY AND
PAYMENT CLASS HAVE ONLY PAYMENT RELATED RESPONSIBILITY (SINGLE RESPONSIBILITY)
"""


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


class PaymentProcessor:

    def pay_credit(self, security_code: str, order: Order):
        print('credit payment processing')
        # if verify_security_code()
        print('security code verified', security_code)
        order.status = 'paid'

    def pay_debit(self, security_code: str, order: Order):
        print('debit payment processing')
        # if verify_security_code()
        print('security code verified', security_code)
        order.status = 'paid'

    # IN FUTURE IF I WANT TO ADD ANOTHER PAYMENT METHOD I HAVE TO TOUCH THIS CLASS ONLY,
    # NOT THE ORDER CLASS


obj = Order()
obj.add_item('vivo', 1, 10000)
obj.add_item('bat', 2, 1000)
obj.add_item('face cream', 2, 499)
print("Total price:", obj.total_price())

payment = PaymentProcessor()
payment.pay_credit('nfafjsdf9yrre4jedgs', obj)
if obj.status == "paid":
    print("payment successful")
