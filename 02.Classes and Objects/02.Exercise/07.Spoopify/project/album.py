from typing import List
from project.song import Song


class Album:
    def __init__(self, name: str, *song: Song):
        self.name = name
        self.song = song
        self.published: bool = False
        self.songs: List = [s for s in song]

    def add_song(self, song: Song):
        # If the song is single, return "Cannot add {song_name}. It's a single"
        # If the album is published, returns "Cannot add songs. Album is published."
        # If the song is already added, return "Song is already in the album."
        # Adds the song to the album and return "Song {song_name} has been added to the album {name}."
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        if self.published:
            return f"Cannot add songs. Album is published."
        if list(filter(lambda x: x.name == song.name, self.songs)):
            return "Song is already in the album."
        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        # If the album is published, returns "Cannot remove songs. Album is published."
        # Remove the song with the given name and return "Removed song {song_name} from album {album_name}."
        # If the song is not in album, returns "Song is not in the album."
        if self.published:
            return "Cannot remove songs. Album is published."
        for s in self.songs:
            if s.name == song_name:
                self.songs.remove(s)
                return f"Removed song {song_name} from album {self.name}."
        return "Song is not in the album."

    def publish(self, ):
        # o	Publishes the album (set to True) and return "Album {name} has been published."
        # o	If the album is published, returns "Album {name} is already published."
        if self.published:
            return f"Album {self.name} is already published."
        self.published = True
        return f"Album {self.name} has been published."

    def details(self, ):
        # Returns the information of the album, with the songs in it, in the format:
        # "Album {name}
        #  == {first_song_info}
        #  == {second_song_info}
        #  …
        #  == {n_song_info}"
        nr = "\n"
        msg = f"Album {self.name}\n"
        msg += nr.join(f"== {s.get_info()}" for s in self.songs)
        return msg
