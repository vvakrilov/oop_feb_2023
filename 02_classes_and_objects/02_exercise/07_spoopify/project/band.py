from typing import List
from project.album import Album


class Band:
    def __init__(self, name: str, ):
        self.name = name
        self.albums: List = []

    def add_album(self, album: Album):
        # Adds an album to the collection and return "Band {band_name} has added their newest album {album_name}."
        # If the album is already added, return "Band {band_name} already has {album_name} in their library."
        # if filter(lambda a: a.name == album.name, self.albums):
        got_album = [a for a in self.albums if a.name == album.name]
        if got_album:
            return f"Band {self.name} already has {album.name} in their library."
        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str):
        # Removes the album from the collection and returns "Album {name} has been removed."
        # If the album is published, returns "Album has been published. It cannot be removed."
        # If the album is not in the collection, returns "Album {name} is not found."
        for a in self.albums:
            if a.name == album_name:
                if a.published:
                    return "Album has been published. It cannot be removed."
                self.albums.remove(a)
                return f"Album {album_name} has been removed."
        return f"Album {album_name} is not found."

    def details(self, ):
        # Returns the information of the band, with their albums, in this format:
        # "Band {name}
        #  {album details}
        #  ...
        #  {album details}"
        nr = "\n"
        msg = f"Band {self.name}\n"
        msg += nr.join(f"{a.details()}" for a in self.albums)
        return msg
