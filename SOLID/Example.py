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

    def pay(self, payment_type: str, security_code: str):
        if payment_type == 'credit':
            print('credit payment processing')
            # if verify_security_code()
            print('security code verified', security_code)
            self.status = 'paid'
        elif payment_type == 'debit':
            print('debit payment processing')
            # if verify_security_code()
            print('security code verified', security_code)
            self.status = 'paid'
        else:
            raise Exception('Invalid payment type')


obj = Order()
obj.add_item('vivo', 1, 10000)
obj.add_item('bat', 2, 1000)
obj.add_item('face cream', 2, 499)
print(obj.total_price())

obj.pay("debit", 'nfafjsdf9yrre4jedgs')
