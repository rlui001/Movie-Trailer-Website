import webbrowser

class Movie():
    def __init__(self, title, image, trailer_url):
        self.title = title
        self.image = image
        self.trailer_url = trailer_url

    def show_trailer(self):
        webbrowser.open(self.trailer_url)
