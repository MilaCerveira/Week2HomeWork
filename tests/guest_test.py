import unittest
from src.room import Room
from src.guest import Guest
from src.song import Song 

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.room1 = Room("The Hypno Room", "Harry Potter", [], 3, 20, 0, [])
        self.guest_1 = Guest("Sam", 100, "Blackbird")
        self.guest_2 = Guest("Ben", 200, "Let it be")
        self.guest_3 = Guest('John', 300, "Sunshine")
        self.guest_4 = Guest("Maria", 250, "Come together")
        self.song_1 = Song("Blackbrid", "IDK", "Gangster rap")
        self.song_2= Song("SOMETHING", "A PERSON", "country")
    
    def test_guest_one_has_name(self):
        self.assertEqual("Sam", self.guest_1.name)
    
    def test_guest_two_has_name(self):
        self.assertEqual("Ben", self.guest_2.name)

    def test_guest_one_has_wallet(self):
        self.assertEqual(100, self.guest_1.wallet)

    def test_guest_two_has_wallet(self):
        self.assertEqual(200, self.guest_2.wallet)

    def test_favourite_song(self):
        self.room1.add_song_to_que(self.song_1.title)
        self.assertEqual("Woooo", self.guest_1.favouriteSong(self, self.room1.songs, self.guest_1.favouriteSong))

    def test_sad(self):
        self.assertEqual("crying", self.guest_1.favouriteSong(self, self.room1.songs, self.guest_1.favouriteSong))
