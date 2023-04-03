from typing import List


class PhotoAlbum:
    pages: int
    photos: List

    def __init__(self, pages: int):
        self.pages = pages
        self.photos = list([] for _ in range(self.pages))
        self._index = 0

    @staticmethod
    def photos_to_pages(photos):
        pages = photos // 4
        if photos % 4 <= 1:
            pages += photos % 4
        else:
            pages += 1
        return pages

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(PhotoAlbum.photos_to_pages(photos_count))

    def add_photo(self, label: str):
        try:
            if len(self.photos[self._index]) == 4:
                self._index += 1
            self.photos[self._index].append(label)
            return f"{label} photo added successfully on page {self._index + 1} slot {len(self.photos[self._index])}"
        except IndexError:
            return "No more free slots"

    def display(self):
        str_repr = ""
        page_edge = "-" * 11
        photo = "[]"
        str_repr += f"{page_edge}\n"
        for page in self.photos:
            str_repr += ' '.join([photo for photos in page if photos]) + "\n"
            str_repr += f"{page_edge}\n"
        return str_repr.rstrip("\n")


# album = PhotoAlbum(4)
# album = PhotoAlbum.from_photos_count(11)
#
# print(album.add_photo("baby"))
# print(album.add_photo("first grade"))
# print(album.add_photo("eight grade"))
# print(album.add_photo("party with friends"))
# print(album.photos)
# print(album.add_photo("prom"))
# print(album.add_photo("wedding"))
# print(album.add_photo("baby"))
# print(album.add_photo("first grade"))
# print(album.add_photo("eight grade"))
# print(album.add_photo("party with friends"))
# print(album.add_photo("baby"))
# print(album.add_photo("first grade"))
# print(album.add_photo("eight grade"))
# print(album.add_photo("party with friends"))
# print(album.photos)
# print(album.display())
