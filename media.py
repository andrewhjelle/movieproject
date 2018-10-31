import webbrowser


class Movie():
    # Creates a shell for a tile to describe a movie with basic characteristics
    # Creates the formatting for a movie tile
    def __init__(
            self, movie_title, date_released, movie_storyline,
            poster_image, trailer_youtube):
        self.title = movie_title
        self.release_date = date_released
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # Creates the ability to launch the movie trailer url
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
