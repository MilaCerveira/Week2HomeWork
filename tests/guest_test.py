import unittest
from src.room import Room
from src.guest import Guest
from src.song import Song 

class TestGuest(unittest.TestCase):
    def setUp(self):
         self.guest_1 = Guest("Guido van Rossum", 300)
         self.guest_2 = Guest("Harry Potter", 200)
    
    def test_guest_one_has_name(self):
        self.assertEqual("Guido van Rossum", self.guest_1.name)
    
    def test_guest_two_has_name(self):
        self.assertEqual("Harry Potter", self.guest_2.name)

    def test_guest_one_has_wallet(self):
        self.assertEqual(300, self.guest_1.wallet)

    def test_guest_two_has_wallet(self):
        self.assertEqual(200, self.guest_2.wallet)

    

 