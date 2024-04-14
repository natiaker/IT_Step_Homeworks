import unittest
from contact_manager import ContactManager


class TestContactManager(unittest.TestCase):
    def setUp(self):
        self.manager = ContactManager()

    def test_add_contact(self):
        self.assertEqual(self.manager.add_contact("Natia", 555555555), "Contact 'Natia' added successfully.")
        self.assertEqual(self.manager.add_contact("Mary", 111111111), "Contact 'Mary' added successfully.")
        self.assertEqual(self.manager.add_contact("John", 222222222), "Contact 'John' added successfully.")
        self.assertEqual(self.manager.add_contact("Natia", 555555555), "Contact 'Natia' already exists.")
        self.assertEqual(self.manager.add_contact("Natia", 999999999), "Contact 'Natia' already exists.")

    def test_remove_contact(self):
        self.manager.add_contact("Helen", 987654321)
        self.manager.add_contact("Bill", 123456789)
        self.assertEqual(self.manager.remove_contact("Helen"), "Contact 'Helen' removed successfully.")
        self.assertEqual(self.manager.remove_contact("Bill"), "Contact 'Bill' removed successfully.")
        self.assertEqual(self.manager.remove_contact("Brad"), "Contact 'Brad' not found.")
        self.assertEqual(self.manager.remove_contact("Michele"), "Contact 'Michele' not found.")

    def test_search_contact(self):
        self.manager.add_contact("Natia", 555555555)
        self.manager.add_contact("Mary", 111111111)
        self.assertEqual(self.manager.search_contact("Mary"),"Name: Mary, Phone Number: 111111111")
        self.assertEqual(self.manager.search_contact("Natia"),"Name: Natia, Phone Number: 555555555")

        self.assertEqual(self.manager.search_contact("Bob"), "Contact 'Bob' not found.")
        self.assertEqual(self.manager.search_contact("James"), "Contact 'James' not found.")