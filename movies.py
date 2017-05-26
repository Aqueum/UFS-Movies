import webbrowser


class Movie:
    """A class to describe movies and launch their trailers"""

    def __init__(self, title, storyline, poster, trailer):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster
        self.trailer_youtube_url = trailer

    def play_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
