class Music:
    def __init__(self, artist, duration, genre, availability):
        self.artist = artist
        self.duration = duration
        self.genre = genre
        self.__availability = availability

    def play(self):
        return f"Now playing a song by {self.artist}."

    def skip(self):
        return f"Skipping the song by {self.artist}."

    def addToPlaylist(self, playlistName):
        return f"The song by {self.artist} was added to {playlistName}."

    def getAvailability(self):
        return self.__availability

    def changeAvailability(self, status):
        self.__availability = status

# Creating two independent objects
song1 = Music("Laufey", 3.45, "Modern Jazz", True)
song2 = Music("The Beatles", 2.30, "Rock", True)

# BEFORE
print("--- BEFORE ---")

print("Song 1:")
print("Artist:", song1.artist)
print("Duration:", song1.duration)
print("Genre:", song1.genre)
print("Available:", song1.getAvailability())

print()

print("Song 2:")
print("Artist:", song2.artist)
print("Duration:", song2.duration)
print("Genre:", song2.genre)
print("Available:", song2.getAvailability())

# Changing only Song 1
print("\nChanging the availability of Song 1...")
song1.changeAvailability(False)

# AFTER
print("\n--- AFTER ---")

print("Song 1:")
print("Artist:", song1.artist)
print("Duration:", song1.duration)
print("Genre:", song1.genre)
print("Available:", song1.getAvailability())

print()

print("Song 2:")
print("Artist:", song2.artist)
print("Duration:", song2.duration)
print("Genre:", song2.genre)
print("Available:", song2.getAvailability())