import unittest
from contact_manager import ContactManager


class TestContactManager(unittest.TestCase):
    def setUp(self):
        # Create a ContactManager instance for testing
        self.manager = ContactManager()

    def test_add_contact(self):
        # Test adding new contacts and checking if they are added successfully
        self.assertEqual(self.manager.add_contact("Natia", 555555555), "Contact 'Natia' added successfully.")
        self.assertEqual(self.manager.add_contact("Mary", 111111111), "Contact 'Mary' added successfully.")
        self.assertEqual(self.manager.add_contact("John", 222222222), "Contact 'John' added successfully.")
        # Test adding an existing contact and checking for the appropriate message
        self.assertEqual(self.manager.add_contact("Natia", 555555555), "Contact 'Natia' already exists.")
        self.assertEqual(self.manager.add_contact("Natia", 999999999), "Contact 'Natia' already exists.")

    def test_remove_contact(self):
        # Add contacts for removal testing
        self.manager.add_contact("Helen", 987654321)
        self.manager.add_contact("Bill", 123456789)

        # Test removing existing contacts and checking for the appropriate message
        self.assertEqual(self.manager.remove_contact("Helen"), "Contact 'Helen' removed successfully.")
        self.assertEqual(self.manager.remove_contact("Bill"), "Contact 'Bill' removed successfully.")
        # Test removing a non-existent contact and checking for the appropriate message
        self.assertEqual(self.manager.remove_contact("Bill"), "Contact 'Bill' not found.")
        self.assertEqual(self.manager.remove_contact("Brad"), "Contact 'Brad' not found.")
        self.assertEqual(self.manager.remove_contact("Michele"), "Contact 'Michele' not found.")

    def test_search_contact(self):
        # Add contacts for searching testing
        self.manager.add_contact("Natia", 555555555)
        self.manager.add_contact("Mary", 111111111)

        # Test searching for existing contacts and checking for the appropriate message
        self.assertEqual(self.manager.search_contact("Mary"),"Name: Mary, Phone Number: 111111111")
        self.assertEqual(self.manager.search_contact("Natia"),"Name: Natia, Phone Number: 555555555")
        # Test searching for non-existent contacts and checking for the appropriate message
        self.assertEqual(self.manager.search_contact("Bob"), "Contact 'Bob' not found.")
        self.assertEqual(self.manager.search_contact("James"), "Contact 'James' not found.")

    def test_display_contacts(self):
        # Test displaying contacts when there are no contacts
        self.assertEqual(self.manager.display_contacts(), "No contacts found.")

        # Add contacts for display testing
        self.manager.add_contact("Mary", 111111111)
        self.manager.add_contact("Bill", 123456789)
        # Test displaying contacts after adding them
        self.assertEqual(self.manager.display_contacts(), f"Name: Mary, Phone Number: 111111111")

        # Remove a contact and test displaying contacts again
        self.manager.remove_contact("Mary")
        self.assertEqual(self.manager.display_contacts(), f"Name: Bill, Phone Number: 123456789")
        self.manager.remove_contact("Bill")
        self.assertEqual(self.manager.display_contacts(), "No contacts found.")


if __name__ == "__main__":
    unittest.main()