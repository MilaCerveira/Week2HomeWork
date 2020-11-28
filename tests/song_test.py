import unittest
from src.room import Room
from src.guest import Guest
from src.song import Song 

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song_1 = Song("Electric Love", "Bjorns", "Indie")
        self.song_2 = Song("Shallow", "Lady Gaga" , "Country Music" )
        self.song_3 = Song("I Wanna Dance with Somebody", "Whitney Houston", "Pop" )
        self.song_4 = Song("X Gona Give It to Ya", "DMX", "Hip-Hop")

    def test_song_has_title(self):
        self.assertEqual("Electric Love", self.song_1.title)
    
    def test_song_has_artist(self):
        self.assertEqual("Bjorns", self.song_1.artist)
    
    def test_song_has_genre(self):
        self.assertEqual("Indie", self.song_1.artist)
