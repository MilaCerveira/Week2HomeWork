class Room :
    def __init__(self, name, guest, songs, capacity, fee, till, occupancy):
        self.name = name 
        self.guest = guest
        self.songs = []
        self.capacity = capacity
        self.fee = 20
        self.till = 0
        self.occupancy = []
   #checkin get guest set put them into empty occupency list    
    def checkin(self, guest):
        if len(self.occupancy) < self.capacity:
            self.occupancy.append(guest)
        else:
            return ("This room is full")
    #checkout get guest remove from occupency list only if that name is in the room
    #put in measures to stop user from checkin a guest out of an empty room
    def checkout(self, guest):
        if self.occupancy <= 0:
             return ("This room is empty")

        if guest in self.occupancy:
            self.occupancy.remove(guest)
        else:
            return("No name found")
