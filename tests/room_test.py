import unittest
from src.room import Room
from src.guest import Guest
from src.song import Song 

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room1 = Room("The Hypno Room", "Harry Potter", [], 3, 20, 0, [])
        self.guest_1 = Guest("Sam", 100, "Blackbird")
        self.guest_2 = Guest("Ben", 200, "Let it be")
        self.guest_3 = Guest('John', 300, "Sunshine")
        self.guest_4 = Guest("Maria", 250, "Come together")
        self.song_1 = Song("Somesong", "IDK", "Gangster rap")
        self.song_2= Song("SOMETHING", "A PERSON", "country")

    
        
    def test_room_has_name(self):
        self.assertEqual("The Hypno Room", self.room1.name)

    def test_room_has_till(self):
        self.assertEqual(0, self.room1.till)

    def check_guest_checkin(self):
        self.room1.checkin(self, self.guest_1.name)
        self.assertEqual(1, len(self.room1.occupancy))
    
    def check_guest_checkin_full(self):
        self.room1.checkin(self, self.guest_1.name)
        self.room1.checkin(self, self.guest_2.name)
        self.room1.checkin(self, self.guest_3.name)
        self.room1.checkin(self, self.guest_4.name)

        self.assertEqual(3, len(self.room1.occupancy))

        #alternative test self.assertEqual("This room is full", self.room1.checkin(self, "Sam" ))
        
    
    def check_remove_guest_from_empty_room(self):
        self.assertEqual("This room is empty", self.room1.checkout(self, self.guest_1.name))

    def check_guest_checkout(self):
        self.room1.checkin(self, self.guest_1.name)
        self.room1.checkout(self, self.guest_1.name)
        self.assertEqual(0, len(self.room1.occupancy))

    def check_guest_out_of_wrong_room(self):
        self.room1.checkin(self, self.guest_1.name)
        self.assertEqual("No name found", self.room1.checkout(self, self.guest_3.name))
        
    
    def check_add_song_to_que(self):
        self.room1.add_song_to_que(self, self.song_1.title)
        self.assertEqual(1, len(self.room1.songs))
    
    def check_song_can_be_removed(self):
        self.room1.remove_song_from_que(self, self.song_1.title)
        self.assertEqual(0, len(self.room1.songs))
    
    def check_payment_can_be_taken(self):
        self.guest_1.wallet = self.room1.pay_fee(self, self.guest_1.wallet)
        self.assertEqual(80, self.guest_1.wallet)
        self.room1.till += self.room1.fee

    