class Room :
    def __init__(self, name, guest, songs, capacity, fee, till, occupancy):
        self.name = name 
        self.guest = guest
        self.songs = []
        self.capacity = 3
        self.fee = 20
        self.till = 0
        self.occupancy = []
        