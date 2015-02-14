import webbrowser

#create Movie class
class Movie():

    #define constructor and instance variables
    def __init__(self, movie_title, year, storyline, director, poster_image, trailer_youtube):
        self.title = movie_title
        self.year = year
        self.storyline = storyline
        self.director = director
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    #define instance method for opening the movie trailer
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
