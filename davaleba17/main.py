class Person:
    def __init__(self, name, deposit=1000, loan=0):
        self.name = name
        self.deposit = deposit
        self.loan = loan

    def __str__(self):
        return f"Person სახელი: {self.name}, დეპოზიტი: {self.deposit}, სესხი: {self.loan}"


class House:
    def __init__(self, ID, price, owner, status="გასაყიდი"):
        self.ID = ID
        self.price = price
        self.owner = owner
        self.status = status


house_owner = Person("John", 5000, 70000)
house_buyer = Person("Mary", 200000, 5000)
house = House(123456, 120000, owner=house_owner)
