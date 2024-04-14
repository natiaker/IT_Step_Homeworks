import unittest
from bank_account import BankAccount


class TestBankAccount(unittest.TestCase):
    def setUp(self):
        # Create BankAccount instance
        self.account = BankAccount("01", "natia", 1000)

    def test_deposit(self):
        # Test depositing a valid amount
        self.assertEqual(self.account.deposit(200), f"Deposited $200. New balance: $1200")
        self.assertEqual(self.account.deposit(1), f"Deposited $1. New balance: $1201")
        # Test depositing zero
        self.assertEqual(self.account.deposit(0), "Invalid amount for deposit.")
        # Test depositing a negative amount
        self.assertEqual(self.account.deposit(-200), "Invalid amount for deposit.")

    def test_withdraw(self):
        # Test withdrawing a valid amount
        self.assertEqual(self.account.withdraw(200), "Withdrew $200. New balance: $800")
        self.assertEqual(self.account.withdraw(5), "Withdrew $5. New balance: $795")
        # Test withdrawing an amount exceeding the balance
        self.assertEqual(self.account.withdraw(900), "Insufficient funds or invalid amount for withdrawal.")
        # Test withdrawing zero
        self.assertEqual(self.account.withdraw(0), "Insufficient funds or invalid amount for withdrawal.")
        # Test withdrawing a negative amount
        self.assertEqual(self.account.withdraw(-20), "Insufficient funds or invalid amount for withdrawal.")
        # Test withdrawing an amount equal to the balance
        self.assertEqual(self.account.withdraw(795), "Withdrew $795. New balance: $0")

    def test_display_balance(self):
        # Check initial balance
        self.assertEqual(self.account.display_balance(), "Current Balance: $1000")
        # Deposit and check if balance displayed correctly
        self.account.deposit(300)
        self.assertEqual(self.account.display_balance(), "Current Balance: $1300")
        # Try depositing a negative amount and check the balance (should not change balance)
        self.account.deposit(-200)
        self.assertEqual(self.account.display_balance(), "Current Balance: $1300")
        # Try depositing zero and check the balance
        self.account.deposit(0)
        self.assertEqual(self.account.display_balance(), "Current Balance: $1300")

        # Withdraw and check if balance displayed correctly
        self.account.withdraw(200)
        self.assertEqual(self.account.display_balance(), "Current Balance: $1100")
        self.account.withdraw(50)
        self.assertEqual(self.account.display_balance(), "Current Balance: $1050")
        # Try withdrawing zero and check the balance
        self.account.withdraw(0)
        self.assertEqual(self.account.display_balance(), "Current Balance: $1050")
        # Try withdrawing an amount exceeding the balance and check the balance
        self.account.withdraw(2000)
        self.assertEqual(self.account.display_balance(), "Current Balance: $1050")


if __name__ == "__main__":
    unittest.main()
