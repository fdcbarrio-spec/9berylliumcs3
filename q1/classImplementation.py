class Music:
    def __init__(self, title, artist, duration, genre, availability):
        self.title = title
        self.artist = artist
        self.duration = duration
        self.genre = genre
        self.__availability = availability

    def play(self):
        return f"Now playing {self.title} by {self.artist}."

    def skip(self):
        return f"Skipping {self.title} by {self.artist}."

    def addToPlaylist(self, playlistName):
        return f"{self.title} by {self.artist} was added to {playlistName}."

    def getAvailability(self):
        return self.__availability

    def changeAvailability(self, status):
        self.__availability = status

# Creating two independent objects
song1 = Music("Lucky for Me", "Laufey", 2.25, "Modern Jazz", True)
song2 = Music("Don't Let Me Down", "The Beatles", 3.35, "Rock", True)

# BEFORE
print("--- BEFORE ---")

print("\nSong 1:")
print("Title:", song1.title)
print("Artist:", song1.artist)
print("Duration:", song1.duration)
print("Genre:", song1.genre)
print("Available:", song1.getAvailability())

print()

print("\nSong 2:")
print("Title:", song2.title)
print("Artist:", song2.artist)
print("Duration:", song2.duration)
print("Genre:", song2.genre)
print("Available:", song2.getAvailability())

# Changing only Song 1
print("\nChanging the availability of Song 1...")
song1.changeAvailability(False)

# AFTER
print("\n--- AFTER ---")

print("\nSong 1:")
print("Title:", song1.title)
print("Artist:", song1.artist)
print("Duration:", song1.duration)
print("Genre:", song1.genre)
print("Available:", song1.getAvailability())

print()

print("\nSong 2:")
print("Title:", song2.title)
print("Artist:", song2.artist)
print("Duration:", song2.duration)
print("Genre:", song2.genre)
print("Available:", song2.getAvailability())