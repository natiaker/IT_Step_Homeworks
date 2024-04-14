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

