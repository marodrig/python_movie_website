class Movie():
    """
    Class representing a Movie.

    """

    def __init__(self, movie_title, storyline, url_poster, url_movie_trailer):
        """
        Constructor for class Movie.

        :param movie_title: movie title.
        :param storyline: description of the storyline for the movie.
        :param url_poster: url of movie poster image.
        :param url_movie_trailer: url of movie trailer.
        :type movie_title: string.
        :type storyline: string.
        :type url_poster: string of url for the poster.
        :type url_movie_trailer: string.

        """
        self.title = movie_title
        self.storyline = storyline
        self.poster_image_url = url_poster
        self.trailer_youtube_url = url_movie_trailer
