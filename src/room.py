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
    # put in measures to check guest is in  that room
    def checkout(self, guest):
        if len(self.occupancy) <= 0:
             return ("This room is empty")

        if guest in self.occupancy:
            self.occupancy.remove(guest)
        else:
            return("No name found")

    def add_song_to_que(self, songName):
        self.songs.append(songName)
    
    def remove_song_from_que(self, songName):
        if len(self.songs) <= 0:
             return ("The queue is empty")

        if songName in self.songs:
            self.songs.remove(songName)
        else:
            return("No song found")

    def pay_fee(self, wallet):
        
        if  wallet >= self.fee:
            wallet -= self.fee
            self.till += self.fee

        return (wallet)
            
        
        #self.room1.pay_fee(self, self.guest_1.wallet)
        #wallet == guest_x.wallet

    
