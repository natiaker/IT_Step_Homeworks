class Person:
    def __init__(self, name, deposit=1000, loan=0):
        self.name = name
        self.deposit = deposit
        self.loan = loan

    def __str__(self):
        return f"სახელი: {self.name}, დეპოზიტი: {self.deposit}, სესხი: {self.loan}"


class House:
    def __init__(self, ID, price, owner, status="გასაყიდი"):
        self.ID = ID
        self.price = price
        self.owner = owner
        self.status = status

    def sell(self, buyer, loan_amount=0):
        if buyer.deposit >= self.price:
            self.owner.deposit += self.price
            self.owner = buyer
            buyer.deposit -= self.price
            self.status = "გაყიდული"
            print(f"{self.ID} ბინა - {self.status}. ახალი მეპატრონე: ({buyer})")
        elif loan_amount > self.price:
            self.owner.deposit += self.price
            self.owner = buyer
            self.status = "გაყიდული სესხით"
            buyer.loan += loan_amount
            print(f"{self.ID} ბინა - {self.status}. ახალი მეპატრონე: ({buyer})")
        else:
            print(f"{buyer.name}ს დეპოზიტზე არ არის საკმარისი თანხა. ({buyer})")


house_owner = Person("ჯონი", 5000, 70000)

house_buyer1 = Person("მარი", 200000)
house1 = House(123456, 120000, house_owner)
house1.sell(house_buyer1)

house_buyer2 = Person("გურამი", 25000, 2000)
house2 = House(789997, 100000, house_owner)
house2.sell(house_buyer2, 120000)

print(f"ბინების მეპატრონე: ({house_owner})")

