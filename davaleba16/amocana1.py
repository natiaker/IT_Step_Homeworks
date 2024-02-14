class BankAccount:
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def transfer(self, money_amount):
        self.balance += money_amount
        print(f"{self.account_holder}ს ანგარიშზე ({self.account_number}) ჩაირიცხა თანხა {money_amount}ლარი. \n"
              f"ბალანსი შეადგენს: {self.balance} ლარს. \n")

    def withdraw(self, money_amount):
        if money_amount <= self.balance:
            self.balance -= money_amount
            print(f"{self.account_holder}ს ანგარიშიდან ({self.account_number}) გავიდა თანხა {money_amount}ლარი. \n"
                  f"ბალანსი შეადგენს: {self.balance} ლარს. \n")
        else:
            print(f"{self.account_holder}ს ანგარიშზე ({self.account_number}) არ არის საკმარისი თანხა.\n"
                  f"ნაშთი შეადგენს: {self.balance} ლარს. \n")


account1 = BankAccount("123456", "ნათია", 1000)
account1.transfer(100)
account1.withdraw(20)

account2 = BankAccount("789012", "ნინო", 2000)
account2.transfer(400)
account2.withdraw(700)
account2.withdraw(1750)
