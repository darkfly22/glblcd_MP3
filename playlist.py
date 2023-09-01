from random import shuffle

class Track:
    def __init__(self, title: str, artiste: str, album: str, duration: str, genre: str, year: str):
        self.title = title
        self.artiste = artiste
        self.album = album
        self.duration = duration
        self.genre = genre
        self.year = year
        
    
# Playlist Class

class Playlist:

    def __init__(self):
        self.playlist = []
    

    def load(self, filename: str):
        with open(filename, 'r') as f:
            
            for track in f:
                trackItem = track.rstrip().split(",")

            self.playlist.append(Track(trackItem[0],trackItem[1], trackItem[2], trackItem[3], trackItem[4],trackItem[5]))
    
    
    def show_tracks(self):
        
        for index, track in enumerate(self.playlist):
            print(f"{index + 1}. {track.title}")
        
    
    def add_track(self, title: str, artiste: str, album: str, duration: str, genre: str, year: str):
        
        self.playlist.append(Track(title, artiste, album, duration, genre, year))
    
    def remove_track(self, title: str):
        songIndex = self.playlist.index(title)
        self.playlist.remove()
    
    def save_playlist(self, filename: str):
        
        try:
            with open(filename + ".txt", 'x') as f:
                for track in self.playlist:
                    f.write()
     
            
   


Playlist = Playlist()
Playlist.add_track("jsvds", "hdsuh", "ee", "eew", "ew")
Playlist.load("tracks.txt")
