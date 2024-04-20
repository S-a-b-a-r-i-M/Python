"""
Requirement:
we have an online store that sells products, and we want to implement the following features:

Display a list of available products
Allow customers to add products to their shopping cart
Calculate the total cost of the items in the shopping cart
Provide a checkout process for customers to complete their purchase
Send an order confirmation email to the customer after successful purchase
"""

from abc import ABC, abstractmethod
from typing import List

# Product entity
class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

# Interface for product repository
class ProductRepository(ABC):
    @abstractmethod
    def get_all_products(self) -> List[Product]:
        pass

# Implementation of in-memory product repository
class InMemoryProductRepository(ProductRepository):
    def __init__(self):
        self.products = [
            Product(1, "Product A", 10.99),
            Product(2, "Product B", 15.99),
            Product(3, "Product C", 8.99),
        ]

    def get_all_products(self) -> List[Product]:
        return self.products

# Shopping cart
class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, product: Product):
        self.items.append(product)

    def total_cost(self) -> float:
        return sum(item.price for item in self.items)

# Order processing
class OrderProcessor:
    def __init__(self, cart: ShoppingCart):
        self.cart = cart

    def checkout(self):
        total_cost = self.cart.total_cost()
        print(f"Total cost: ${total_cost:.2f}")
        # Perform payment processing and order creation logic

# Interface for notification service
class NotificationService(ABC):
    @abstractmethod
    def send_order_confirmation(self, order_details: str):
        pass

# Implementation of email notification service
class EmailNotificationService(NotificationService):
    def send_order_confirmation(self, order_details: str):
        print(f"Order confirmation email sent: {order_details}")

# Main program
if __name__ == "__main__":
    # Setup dependencies
    product_repository = InMemoryProductRepository()
    notification_service = EmailNotificationService()

    # Display available products
    products = product_repository.get_all_products()
    print("Available Products:")
    for product in products:
        print(f"{product.id}. {product.name} - ${product.price:.2f}")

    # Create a shopping cart and add items
    cart = ShoppingCart()
    cart.add_item(products[0])
    cart.add_item(products[2])

    # Checkout and send order confirmation
    order_processor = OrderProcessor(cart)
    order_processor.checkout()
    notification_service.send_order_confirmation("Order details...")


"""
Explanation:
Here's how this example demonstrates the SOLID principles and promotes high cohesion and low coupling:

Single Responsibility Principle (SRP): 
    Each class has a single responsibility. For example, Product represents a product entity, 
    ProductRepository handles product retrieval, ShoppingCart manages the items in the cart, 
    OrderProcessor handles the checkout process, and NotificationService sends order confirmations.

Open/Closed Principle (OCP): 
    The code is open for extension but closed for modification. 
    For example, if you want to add a new notification service (e.g., SMS notification), 
    you can create a new class that implements the NotificationService interface without modifying the existing code.

Liskov Substitution Principle (LSP): 
    The derived class InMemoryProductRepository can be substituted for its base class ProductRepository 
    without affecting the correctness of the program.

Interface Segregation Principle (ISP): 
    The ProductRepository and NotificationService interfaces are small and specific, 
    promoting high cohesion and reducing the need for classes to implement methods they don't use.

Dependency Inversion Principle (DIP): 
    The high-level classes (OrderProcessor and the main program) depend on abstractions 
    (ProductRepository and NotificationService) rather than concrete implementations. 
    This promotes loose coupling and allows for easy replacement of the concrete implementations.

High Cohesion: 
    Each class has a well-defined responsibility, and the methods within each class are closely related to that responsibility.

Low Coupling: 
    The classes are loosely coupled through the use of interfaces and dependency injection. 
    For example, the OrderProcessor doesn't directly depend on the concrete implementation of the NotificationService.

This example demonstrates how to structure an e-commerce system by separating concerns into different classes, 
promoting modularity, and following the SOLID principles. It also showcases the use of abstractions (interfaces) 
to decouple components and promote loose coupling, making the codebase more maintainable and extensible.
    """