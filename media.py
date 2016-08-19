import webbrowser

class Movie():
    """ The Movie class stores a movie's details. i.e. Title, image, trailer url\n   """
    def __init__(self, title, image, trailer_youtube_url):
        self.title = title
        self.poster_image_url = image
        self.trailer_youtube_url = trailer_youtube_url

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
