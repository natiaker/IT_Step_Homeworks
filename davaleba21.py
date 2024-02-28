# Create Product class
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


# create product instances
product1 = Product('Banana', 3.00, 2)
product2 = Product('Orange', 4.50, 4)
product3 = Product('Apple', 2.20, 12)
product4 = Product('Kiwi', 3.00, 7)

lst = [product1, product2, product3, product4]

print(lst)