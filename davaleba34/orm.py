from datetime import datetime

from model import session, Products, Categories, Orders


def insert_product(name, price, quantity, category_id):
    new_product = Products(product_name=name, product_price=price, stock_quantity=quantity, category_id=category_id)
    session.add(new_product)
    session.commit()


def insert_category(name):
    new_category = Categories(category_name=name)
    session.add(new_category)
    session.commit()


# insert_category("Fruits")
# insert_category("Electronics")
# insert_category("Furniture")


# insert_product("Apple", 3,50, 1)
# insert_product("Mobile", 800, 15,2)
# insert_product("Laptop", 1200, 20, 2)
# insert_product("Pear", 3.5, 40, 1)
# insert_product("Chair", 35, 27, 3)


def delete_product(name):
    product_to_delete = session.query(Products).filter_by(product_name=name).first()

    if product_to_delete:
        session.delete(product_to_delete)
    else:
        print("Product not found")


# delete_product("Pear")


def update_product(name, new_name):
    product_to_update = session.query(Products).filter_by(product_name=name).first()
    if product_to_update:
        product_to_update.product_name = new_name
        session.commit()
    else:
        print("Product not found")


# update_product("Chair", "Table")


def place_order(product_name, quantity):
    product = session.query(Products).filter_by(product_name=product_name).first()
    if product:
        if product.stock_quantity >= quantity:
            product.stock_quantity -= quantity
            new_order = Orders(product_id=product.product_id, quantity=quantity, order_date=datetime.now(), status="pending")
            session.add(new_order)
            session.commit()
            print("Order placed successfully")
        else:
            print("Not enough in stock")
    else:
        print("Product not found")


# place_order("Apple", 4)
# place_order("Mobile", 1)

joined_products = session.query(Products.product_id, Products.product_name, Products.product_price,
                                Products.stock_quantity, Categories.category_name, Orders.order_id, Orders.quantity,
                                Orders.order_date, Orders.status).join(Orders).join(Categories).filter(Orders.status ==
                                                                                                       'pending')

# print(joined_products)

for product in joined_products:
    print(product)

# session.commit()
