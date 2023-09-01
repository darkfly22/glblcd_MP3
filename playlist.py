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
        print(self.playlist)    
    
    def show_tracks(self):
        
        for index, track in enumerate(self.playlist):
            print(f"{index + 1}. {track.title}")
        
    
    def add_track(self, title: str, artiste: str, album: str, duration: str, genre: str, year: str):
        
        self.playlist.append(Track(title, artiste, album, duration, genre, year))
    
    def remove_track(self, title: str):
        songIndex = self.playlist.index(title)
        self.playlist.remove()
    
    def save_playlist(self, filename):
        
        try:
            new = open(filename + ".txt", 'x')
        except FileExistsError:
            print("Playlist already exists, choose another name")
        
        else:
            for track in self.playlist:
                new.write(f"{track.title}, {track.artiste} {track.album} {track.duration} {track.genre}, {track.year}, \n")
            new.close()
            
    
    def shuffle_playlist(self):
        shuffle(self.playlist)
    
    def count_tracks(self):
        print(f"There are {len(self.playlist)} in the playlist")
        
    def total_duration(self):
        total = 0
        for track in self.playlist:
            duration = track.duration.split(":")
            seconds = int(duration[0]) * 60 + int(duration[1])
            total += seconds
        
        
        print(f"The total duration of this playlist is {total//60} minutes, {total%60}seconds")         
            
        
    def reset(self):
        self.playlist = []
        
    def is_empty(self):
        
        return "Playlist is empty" if len(self.playlist) == 0 else "Playlist is not empty"


Playlist = Playlist()
Playlist.add_track("jsvds", "hdsuh", "ee", "eew", "ew")
Playlist.load("tracks.txt")
