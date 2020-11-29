class Guest :
    def __init__(self, name, wallet, favouriteSong):
        self.name = name
        self.wallet = wallet
        self.favouriteSong = favouriteSong
        
    def check_playlist_for_favourite_song(self, playlist, favourite):
        #read over all song on list
            #if fav == current item
               #return woooo

        #return empty

        for song in playlist:
            if song == favourite:
                return("Woooo")

        if song != favourite:
            return("crying")
            