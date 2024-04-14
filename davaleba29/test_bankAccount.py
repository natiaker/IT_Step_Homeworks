import unittest
from bank_account import BankAccount


class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.account = BankAccount("01", "natia", 1000)

    def test_deposit(self):
        self.assertEqual(self.account.deposit(200), f"Deposited $200. New balance: $1200")
        self.assertEqual(self.account.deposit(1), f"Deposited $1. New balance: $1201")
        self.assertEqual(self.account.deposit(0), "Invalid amount for deposit.")
        self.assertEqual(self.account.deposit(-200), "Invalid amount for deposit.")

