import unittest
from src.room import Room
from src.guest import Guest
from src.song import Song 

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room_1 = Room("The Hypno Room", "Harry Potter", [], 3, 20, 0, [])
        

    def check_guest_checkin
        self.room1.checkin("test")
        self.assertEqual(1, self.room1.occupancy.len())
    
    def check_guest_checkin_full
    
    def check_remove_guest_from_empty_room

    def check_guest_checkout
        self.room1.checkout("test")
        self.assertEqual(0, self.room1.occupancy.len())

    def test_room_has_name(self):
        self.assertEqual("The Hypno Room", self.room_1.name)

    def test_room_has_till(self):
        self.assertEqual(0, self.room_1.till)
