# Create Product class
import json


class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f'Product name: {self.name}, price: {self.price}, quantity: {self.quantity}'


# create product instances
product1 = Product('Banana', 3.00, 2)
product2 = Product('Orange', 4.50, 4)
product3 = Product('Apple', 2.20, 12)
product4 = Product('Kiwi', 3.00, 7)

# add products to list
lst = [product1, product2, product3, product4]

print("List products: ")
for product in lst:
    print(product)


# create serialization method
def serialization_func(obj):
    if isinstance(obj, Product):
        return {"Name": obj.name, "Price": obj.price, "Quantity": obj.quantity}
    raise TypeError(f"Object is not type of Product")


# translate product class into json and write in a file
with open("products.json", "w") as json_file:
    json.dump(lst, json_file, default=serialization_func, indent=4)


# create deserialization method
def deserialization_func(json_obj):
    return Product(json_obj['Name'], json_obj['Price'], json_obj["Quantity"])


# Read products file, translate json into Product class
with open("products.json", "r") as file:
    product_data = json.load(file, object_hook=deserialization_func)

# Print all products information
print("\nDeserialized products: ")
for product in product_data:
    print(product)
