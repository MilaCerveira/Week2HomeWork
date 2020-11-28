import unittest
from src.room import Room
from src.guest import Guest
from src.song import Song 

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.name = Name("The Hypno Room")
        self.songs = []
        self.guest = Guest
        self.song = Song
        self. capacity = 3
        self.till = 0
        self.occupancy = []



    def test_room_has_name(self):
        self.assertEqual("The Hypno Room", self.room.name)

    def test_room_has_till(self):
        self.assertEqual(100, self.room.till)
